import asyncio
import socket
import struct
import os
import random
import time

FLAGS_FIN = 1<<0
FLAGS_SYN = 1<<1
FLAGS_RST = 1<<2
FLAGS_ACK = 1<<4

ETH_P_ALL = 0x0003
ETH_P_IP  = 0x0800

#TCP
MSS = 1460
K = 4.0
G = 1.0
SRTT = 0.0
RTTVAR = 0.0
alpha = 1.0/8.0
beta = 1.0/4.0

enviados = []

ICMP = 0x01  # https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers


# Coloque aqui o endereço de destino para onde você quer mandar o ping
# Pode ser obtido com o comando arp -a | grep _gateway
dest_ip = '192.168.1.1'

# Coloque abaixo o endereço IP do seu computador na sua rede local
# Pode ser obtido com o comando ifconfig
src_ip = '192.168.1.116'

# Coloque aqui o nome da sua placa de rede
# Pode ser obtido com o comando ifconfig
if_name = 'wlp2s0'

# Coloque aqui o endereço MAC do roteador da sua rede local (arp -a | grep _gateway)
# Pode ser obtido com o comando arp -a | grep _gateway
dest_mac = '7c:8b:ca:3d:01:8e'

# Coloque aqui o endereço MAC da sua placa de rede (ip link show dev wlan0)
# Pode ser obtido com  ip link show dev <nomePlacaDeRede> 
src_mac = '28:e3:47:b0:6f:fa'

# Fragmentos recebido
receivedPackages = {}

#inicializacao da variavel para syncio.get_event_loop().call_later()
#para o descartar de fragmentos
discard = None 

class Conexao:
    def __init__(self, id_conexao, seq_no, ack_no):
        self.id_conexao = id_conexao #ID da conexao
        self.seq_no = seq_no #num de sequencia
        self.ack_no = ack_no #ACK
        self.send_base = seq_no # base
        self.first_ack = True   # significa que o handshake ainda nao acabou
        self.timer = None # objeto timer da conexao
        self.start_t = 0 # tempo de inicio da conexao
        self.end_t = 0 # tempo de fim da conexao
        self.RTO = 3.0 # timeout
        self.last_RTT = 0.0 # ultimo RTT
        self.curr_RTT = 0.0 # RTT atual
        self.rwnd = self.cwnd = 2*MSS #receiver window e congestion window
        self.rx_win = 1024 # janela de transmissao
        self.ssthresh = 10*MSS # janela limite
        self.state = "Slow Start" # estado par a maquina de estadoss
        self.last_ack = self.send_base #ultimo ack aceito
        self.send_queue = b"HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\n" + 100000 * b"hello pombo\n"
        self.no_ack_queue = b"" 
        self.sent = []  #enviados
        self.flag_fin = False # flag fin
        self.flag_handshake = True # handshake
        self.flag_close_conection = False # fechar conexao
        self.store_time = {} # armazena os times
conexoes = {}

def ip_addr_to_bytes(addr):
    return bytes(map(int, addr.split('.')))

def addr2str(addr):
    return '%d.%d.%d.%d' % tuple(int(x) for x in addr)

def str2addr(addr):
    return bytes(int(x) for x in addr.split('.'))

def mac_addr_to_bytes(addr):
    return bytes(int('0x'+s, 16) for s in addr.split(':'))

def handle_ipv4_header(packet):
    version = packet[0] >> 4
    ihl = packet[0] & 0xf
    assert version == 4
    src_addr = addr2str(packet[12:16])
    dst_addr = addr2str(packet[16:20])
    segment = packet[4*ihl:]
    return src_addr, dst_addr, segment

def make_synack(src_port, dst_port, seq_no, ack_no):
    return struct.pack('!HHIIHHHH', src_port, dst_port, seq_no,
                       ack_no, (5<<12)|FLAGS_ACK|FLAGS_SYN,
                       1024, 0, 0)

def calc_checksum(segment):
    if len(segment) % 2 == 1:
        segment += b'\x00'
    checksum = 0
    for i in range(0, len(segment), 2):
        x, = struct.unpack('!H', segment[i:i+2])
        checksum += x
        while checksum > 0xffff:
            checksum = (checksum & 0xffff) + 1
    checksum = ~checksum
    return checksum & 0xffff

def fix_checksum(segment, src_addr, dst_addr):
    pseudohdr = str2addr(src_addr) + str2addr(dst_addr) + \
        struct.pack('!HH', 0x0006, len(segment))
    seg = bytearray(segment)
    seg[16:18] = b'\x00\x00'
    seg[16:18] = struct.pack('!H', calc_checksum(pseudohdr + seg))
    return bytes(seg)

def cria_synack(conexao):
    (src_addr, src_port, dst_addr, dst_port) = conexao.id_conexao
    return struct.pack('!HHIIHHHH', dst_port, src_port, conexao.seq_no, conexao.ack_no, (5<<12)|FLAGS_ACK|FLAGS_SYN,1024, 0, 0)

def cria_ack(conexao):
    (src_addr, src_port, dst_addr, dst_port) = conexao.id_conexao
    return struct.pack('!HHIIHHHH', dst_port, src_port, conexao.seq_no, conexao.ack_no, (5<<12)|FLAGS_ACK,1024, 0, 0)

def cria_fin(conexao):
    (src_addr, src_port, dst_addr, dst_port) = conexao.id_conexao
    return struct.pack('!HHIIHHHH', dst_port, src_port, conexao.seq_no, conexao.ack_no, (5<<12)|FLAGS_FIN|FLAGS_ACK,1024, 0, 0)

def enviaSrc(fd, conexao, segment):
    (src_addr, src_port, dst_addr, dst_port) = conexao.id_conexao
    send_ip(fd, segment, ICMP)

def enviaDst(fd, conexao, segment):
    (src_addr, src_port, dst_addr, dst_port) = conexao.id_conexao
    send_ip(fd, segment, ICMP)

def send_eth(fd, datagram, protocol):
    eth_header = mac_addr_to_bytes(dest_mac) + \
        mac_addr_to_bytes(src_mac) + \
        struct.pack('!H', protocol)

    fd.send(eth_header + datagram)

ip_pkt_id = 0
def send_ip(fd, msg, protocol):
    global ip_pkt_id
    ip_header = bytearray(struct.pack('!BBHHHBBH',
                            0x45, 0,
                            20 + len(msg),
                            ip_pkt_id,
                            0,
                            15,
                            protocol,
                            0) +
                          ip_addr_to_bytes(src_ip) +
                          ip_addr_to_bytes(dest_ip))
    ip_header[10:12] = struct.pack('!H', calc_checksum(ip_header))
    ip_pkt_id += 1
    send_eth(fd, ip_header + msg, ETH_P_IP)


def transmit_as_allowed(fd, conexao):
    print("Sending...")

    tx_win = min(conexao.rwnd, conexao.cwnd)
    amount_to_transmit = max(0, tx_win - len(conexao.sent))
    data_to_transmit = conexao.send_queue[:amount_to_transmit]
    conexao.send_queue = conexao.send_queue[amount_to_transmit:]
    conexao.sent.append(data_to_transmit) 

    (dst_addr, dst_port, src_addr, src_port) = conexao.id_conexao

    for i in range(0, len(data_to_transmit), MSS):
        payload = data_to_transmit[i:i+MSS]

        segment = struct.pack('!HHIIHHHH', src_port, dst_port, conexao.seq_no,
                              conexao.ack_no, (5<<12)|FLAGS_ACK,
                              1024, 0, 0) + payload

        conexao.seq_no = (conexao.seq_no + len(payload)) & 0xffffffff

        enviaDst(fd, conexao, segment)
    
    #FILA DE DADOS vazia - acabou o envio (envia um pacote com a flag FIN)
    if conexao.send_queue == b"":
        print("Acabou! - Precisa mandar a FIN")
        segment = struct.pack('!HHIIHHHH', src_port, dst_port, conexao.seq_no,conexao.ack_no, (5<<12)|FLAGS_FIN|FLAGS_ACK,0, 0, 0)
        enviaDst(fd, conexao, segment)
        # Temos que fechar a conexao


    else:
        print("Proximo envio")
        asyncio.get_event_loop().call_later(.001, transmit_as_allowed, fd, conexao) 

    last_ack = conexao.ack_no      

#Trata recebimento do ack_no
def ack_recv(fd, conexao, ack_no):
    print("Entrou em ack_recv")
    print("ack_no = " + str(ack_no))
    print("con.send_base = " + str(conexao.send_base))
    if(ack_no > conexao.send_base):
        print("Entrou no ack >")
        ###############################################
        # Trata o handshake
        if(conexao.flag_handshake == True):
            conexao.send_base = ack_no
            conexao.flag_handshake = False

            print("Conexao estabelecida...\n")
        ###############################################
        
        ###############################################
        # Trata o recebimento de ACK apos receber a flag de FIN
        elif(conexao.flag_fin):
            conexao.send_base = ack_no
            print("Conexao encerrada")
        ###############################################



        ###############################################
        # Trata o recebimento de ACK sem ser no handshake inicial ou final
        else:
            #Dados confirmados a serem removidos da noAck_
            print("Confirmando ack: \n", ack_no)
            qtd_dados_reconhecidos = ack_no - conexao.send_base
            print("Dados reconhecidos: \n", qtd_dados_reconhecidos)
            #Atualiza send_base
            conexao.send_base = ack_no

            #Remove da fila de enviados sem confirmacao
            if conexao.send_queue == b'' :
                #Se houver intencao de fechar conexao, essa acao e realizada
                if conexao.flag_close_conection :
                    #Enviando fechamento de conexao
                    segment = cria_fin
                    enviaSrc(fd, conexao, segment)
                    conexao.seq_no += 1

def transportLayer(packet):

    print("\n****Transport Layer****\n")

    src_addr, dst_addr, segment = handle_ipv4_header(packet)
    src_port, dst_port, seq_no, ack_no, \
        flags, window_size, checksum, urg_ptr = \
        struct.unpack('!HHIIHHHH', segment[:20])
    
    #conta acks duplicados
    dup_ack_cnt = 0

    id_conexao = (src_addr, src_port, dst_addr, dst_port)

    #if not(dst_port == 7000 or dst_port == 8000):
    #    return

    payload = segment[4*(flags>>12):]

    # Tratamento da FLAG SYN indica o inicio do handshake de conexao
    if (flags & FLAGS_SYN) == FLAGS_SYN:
        print('%s:%d -> %s:%d (seq=%d)' % (src_addr, src_port,dst_addr, dst_port, seq_no))

        conexoes[id_conexao] = conexao = Conexao(id_conexao=id_conexao,
                                                 seq_no=struct.unpack('I', os.urandom(4))[0],
                                                 ack_no=seq_no + 1)

        conexao.store_time[conexao.seq_no] = time.time()
        # Envio do aceite de conexao - SYNACK
        segment = cria_synack(conexao)
        enviaSrc(fd, conexao, segment)

        conexao.seq_no += 1
        asyncio.get_event_loop().call_later(.1, transmit_as_allowed, fd, conexao)

    # Se a conexao ja existe
    elif id_conexao in conexoes:
        conexao = conexoes[id_conexao]
        # Tratamento da FLAG FIN - indica o inicio do handshake de finalizacao
        if (flags & FLAGS_FIN) == FLAGS_FIN:
            conexao.flag_fin = True
            print("Flag de FIN recebida")
            # Verifica se ja recebeu tudo
            if conexao.ack_no == seq_no:
            # Se tiver recebido tudo certo ate aqui, incrementa 1 para informar que e um ACK do FIN
                conexao.ack_no += 1
            # Senao, o valor de ack_no tere sido mantido, fazendo com que a outra ponta saiba onde paramos de receber dados
            segment = cria_ack(conexao)
            enviaSrc(fd, conexao, segment)

        if (flags & FLAGS_ACK) == FLAGS_ACK:
            ack_recv(fd, conexao, ack_no)

            # codigo relacionado a transmissao
            #Maquina de Estados e Comportamento
            #SLOW START
            if conexao.state == "Slow Start":
                print("Estado: Slow Start")
                #handshacking
                if conexao.first_ack:
                    if ack_no == conexao.send_base + 1:
                        conexao.send_base = ack_no
                        conexao.first_ack = False
                        transmit_as_allowed(fd,conexao)
                #Transicao
                elif conexao.cwnd >= conexao.ssthresh:
                        conexao.state = "Congestion Avoidance"
                #NEW ACK no Slow Start
                elif ack_no == conexao.send_base:
                    conexao.cwnd = conexao.cwnd + MSS
                    conexao.last_ack = ack_no
                    dup_ack_cnt = 0
                    transmit_as_allowed(fd,conexao)
                #Duplicado
                elif ack_no == conexao.last_ack:
                    dup_ack_cnt = dup_ack_cnt + 1
                #3 acks duplicados
                elif dup_ack_cnt == 3:
                    conexao.state = "Fast Recovery"
                    conexao.ssthresh = conexao.cwnd//2
                    cwnd = ssthresh + 3
                    # se duplicou 3 vezes tenta retransmitir
                    conexao.timer = asyncio.get_event_loop().call_later(conexao.RTO, retransmition, fd, conexao)
                #Timeout 
                elif ack_no > conexao.send_base:
                    #DONE: descartar ack_no - conexao.send_base da fila de enviados
                    del enviados[ack_no - conexao.send_base]
                    conexao.send_base = ack_no
                    if conexao.timer is not None:
                        conexao.timer.cancel()
                    if len(conexao.sent) > 0:
                        conexao.timer = asyncio.get_event_loop().call_later(conexao.RTO, retransmition, fd, conexao)

            #CONGESTION AVOIDANCE
            if conexao.state == "Congestion Avoidance":
                print("Estado: Congestion Avoidance")
                #NEW ACK no Congestion Avoidance
                if ack_no == conexao.send_base:
                    conexao.cwnd = conexao.cwnd + MSS*(MSS//conexao.cwnd)
                    conexao.last_ack = ack_no
                    dup_ack_cnt = 0
                    transmit_as_allowed(fd,conexao)
                #Ack duplicado
                elif ack_no == conexao.last_ack:
                    dup_ack_cnt = dup_ack_cnt + 1
                #3 acks duplicados
                elif dup_ack_cnt == 3:
                    conexao.state = "Fast Recovery"
                    conexao.ssthresh = conexao.cwnd//2
                    cwnd = ssthresh + 3
                    # se duplicou 3 vezes tenta retransmitir
                    conexao.timer = asyncio.get_event_loop().call_later(conexao.RTO, retransmition, fd, conexao)
                #Timeout
                elif ack_no > conexao.send_base:
                    #DONE: descartar ack_no - conexao.send_base da fila de enviados
                    del enviados[ack_no - conexao.send_base]
                    conexao.send_base = ack_no
                    if conexao.timer is not None:
                        conexao.timer.cancel()
                    if len(conexao.sent) > 0:
                        conexao.timer = asyncio.get_event_loop().call_later(conexao.RTO, retransmition, fd, conexao)

            #FAST RECOVERY
            if conexao.state == "Fast Recovery":
                print("Estado: Fast Recovery")
                #tratamento de ack duplicado
                if ack_no == conexao.last_ack:
                    conexao.cwnd = conexao.cwnd + MSS
                    transmit_as_allowed(fd,conexao)
                #NEW ACK no fast recovery
                elif ack_no == conexao.send_base:
                    conexao.cwnd = conexao.ssthresh
                    conexao.last_ack = ack_no
                    dup_ack_cnt = 0
                    conexao.state = "Congestion Avoidance"
                #Timeout
                elif ack_no > conexao.send_base:
                    #DONE: descartar ack_no - conexao.send_base da fila de enviados
                    del enviados[ack_no - conexao.send_base]
                    conexao.send_base = ack_no
                    if conexao.timer is not None:
                        conexao.timer.cancel()
                    if len(conexao.sent) > 0:
                        conexao.timer = asyncio.get_event_loop().call_later(conexao.RTO, retransmition, fd, conexao)
  
        # Tratamento do payload maior que 0
        if len(payload) > 0:
            # codigo relacionado a recepcao
            if conexao.seq_no == conexao.ack_no:
                conexao.ack_no += len(payload)

                segment = cria_ack(conexao)
                enviaSrc(fd, conexao, segment)
    else:
        print('%s:%d -> %s:%d (pacote associado a conexao desconhecida)' %
            (src_addr, src_port, dst_addr, dst_port))

def raw_recv(fd):
    frame = fd.recv(12000)
    
    print("\n =========================== \n")

    #Verifica MAC e Protocol
    if verify_MAC(frame) and verify_protocol(frame):
        print('recebido quadro de %d bytes' % len(frame))
        print(repr(frame))

        #Obtem o Datagram
        datagram = frame[14:]

        #Obtem a mensagem fragmentada
        defragMSG = defrag(datagram)

        #Isso impede que o um fragmento de mensagem va para o
        #transportLayer
        if defragMSG is not None:
            #vai para a camada de transporte
            transportLayer(defragMSG)

    else:
        print("Nao passou na verificacao")

#Calcula o RTO da conexao
def RTO(conexao):
    conexao.last_RTT = conexao.curr_RTT

    conxao.curr_RTT = conexao.curr_RTT + conexao.end_t

    #timeout
    #primeira vez
    if conexao.last_RTT == 0.0:
        print("Primeiro RTT")
        SRTT = conexao.curr_RTT  
        RTTVAR = conexao.curr_RTT/2 
        conexao.RTO = SRTT + max(G, K*RTTVAR)
    else:#Se houver um rtt subsequente
        RTTVAR = (1 - beta)*RTTVAR + beta*abs(SRTT - conexao.curr_RTT)#12.5
        print("RTTVAR: " + str(RTTVAR))
        SRTT = (1 - alpha)*SRTT + alpha*conexao.curr_RTT
        print("SRTT: " + str(SRTT))
        conexao.RTO = SRTT + max(G, K*RTTVAR)

        #Corrige os limites do RTO
        if conexao.RTO < 1.0:
            conexao.RTO = 1.0
        if conexao.RTO > 60.0:
            conexao.RTO = 60.0

def retransmition(fd,conexao):
    (dst_addr, dst_port, src_addr, src_port) = conexao.id_conexao
    print("RETRANSMIT...")

    #Maquina de estados
    if conexao.state == "Slow Start":
        conexao.ssthresh = conexao.cwnd//2
        conexao.cwnd = MSS
        dup_ack_cnt = 0
    elif conexao.state == "Congestion Avoidance":
        conexao.ssthresh = conexao.cwnd//2
        conexao.cwnd = MSS
        dup_ack_cnt = 0 
        conexao.state = "Slow Start"
    elif conexao.state == "Fast Recovery":
        conexao.ssthresh = conexao.cwnd//2
        conexao.cwnd = 1
        dup_ack_cnt = 0
        conexao.state = "Slow Start"

    data_to_retransmit = conexao.sent[0]
    conexao.sent.append(data_to_retransmit)
    for i in range(0, len(data_to_retransmit), MSS):
        payload = data_to_retransmit[i:i+MSS]
        segment = struct.pack('!HHIIHHHH', src_port, dst_port, conexao.seq_no,
                                  conexao.ack_no, (5<<12)|FLAGS_ACK,
                                  1024, 0, 0) + payload

        conexao.seq_no = (conexao.seq_no + len(payload)) & 0xffffffff

    enviaDst(fd, conexao, segment)

def verify_MAC(frame):
    print("\n****Verificando MAC addr****\n")

    dest_mac_bytes = frame[0:6]
    src_mac_bytes  = mac_addr_to_bytes(src_mac)

    print("MAC de destino : ", ':'.join('%02x'%x for x in dest_mac_bytes))
    print("Meu MAC : ", ':'.join('%02x'%x for x in src_mac_bytes))

    if dest_mac_bytes == src_mac_bytes:
        return True
    else:
        return False

def verify_protocol(frame):
    print("\n****Verficando o protocolo****\n")
    protocol_bytes = frame[12:14]

    print("Protocolo do Frame : ", protocol_bytes)
    print("Protocolo IP:  ", struct.pack('!H', ETH_P_IP))

    if protocol_bytes == struct.pack('!H', ETH_P_IP):
        return True
    else:
        return False

def calc_checksum(segment):
    if len(segment) % 2 == 1:
        # se for ímpar, faz padding à direita
        segment += b'\x00'
    checksum = 0
    for i in range(0, len(segment), 2):
        x, = struct.unpack('!H', segment[i:i+2])
        checksum += x
        while checksum > 0xffff:
            checksum = (checksum & 0xffff) + 1
    checksum = ~checksum
    return checksum & 0xffff

def discard_packet(idTuple):

    print("******************DESCARTANDO ", idTuple, " POR TIMEOUT*****************\n")
    for tuple in receivedPackages:
       if idTuple[0] == tuple[0] and idTuple[1] == tuple[1] and idTuple[2] == tuple[2] and idTuple[3] == tuple[3] and idTuple[4] == tuple[4]:
           del receivedPackages[tuple]

def defrag(packet):

    global discard
    global lastTuple

    #Chegou um pacote, cancela o timeout
    discard.cancel()

    #Se o pacote for a mensagem inteira, retorna ele inteiro
    appendedMsg = packet

    packetFlag = packet[6] & 0b11100000

    #o offset ocupa mais de um byte, para isso pega o nibble
    #menos significativo e calcula junto com o segundo byte
    offset = (packet[6] & 0b00011111)*256 + packet[7]

    #o flag de fragmentacao fica 32 se ha mais fragamentos ou 0 para o ultimo pacote de fragmentacao.
        #64 se nao precisa de fragmentacao
    if packetFlag == 32 or (packetFlag == 0 and offset > 0):

        #o id da mensagem ocupa dois bytes do cabecalho, para ter o numero de id e
        #necessario calcular o numero desses 2 bytes
        id = packet[4]*256 + packet[5]



        #os byte 12, 13, 14 e 15 sao o endereco de destino da mensagem, para
        #identificar de qual mensagem pertence o fragamentos
        #usa o endereco, o id e o offset(para verificar qual parte da mensagem e)
        idTuple = (packet[12], packet[13], packet[14], packet[15], id, offset)
        lastTuple = idTuple

        #se o pacote nao e repetido, adiciona na lista de pacotes recebidos
        if not idTuple in receivedPackages:
            receivedPackages[idTuple] = packet

        #Se a mensagem nao esta completa, nao retorna nada da mensagem
        appendedMsg = None

        #checa se todos os pacotes da mensagem chegaram, se chegaram desfragmente a mensagem
        if checkAllPackets(idTuple):
            #se a mensagem esta completa, retorne-a
            appendedMsg = appendPackets(idTuple)

        #Inicia a espera por outro pacote
        discard = asyncio.get_event_loop().call_later(3, discard_packet, idTuple)

    return appendedMsg

def checkAllPackets(idTuple):
    numberOfPackets = 0
    totalOfPackets = 0
    allPackets = False

    #para cada tupla de identificacao da lista de pacotes recebidos, 
    #verifica se a tupla e relacionada ao pacote recebidos
    #verificando o endereco de origem e o id da mensagem
    for tuple in receivedPackages:
        if idTuple[0] == tuple[0] and idTuple[1] == tuple[1] and idTuple[2] == tuple[2] and idTuple[3] == tuple[3] and idTuple[4] == tuple[4]:

            #conta todos os pacotes da mesma mensagem
            numberOfPackets = numberOfPackets + 1

            #se for o ultimo pacote da mensagem, e possivel saber quantos pacotes a mensagem total tem
            packetFlag = receivedPackages[tuple][6] & 0b11100000
            if packetFlag == 0:
                #cada offset do pacote e multiplo de 185, entao e possivel saber quantos 
                #pacotes anteriores chegaram com o offset do ultimo pacote
                totalOfPackets = tuple[5]/185 + 1
                #print(tuple[5]*8 + 764) verificar o tamanho total da mensagem

    #se o total de pacotes recebidos for o numero total de pacotes da mensagem, entao 
    #foram recebido todos os pacotes da mensagem
    if totalOfPackets > 0 and numberOfPackets == totalOfPackets:
        print("Recebidos todos os", int(totalOfPackets), "pacotes da mensagem",idTuple[4], "vinda de", idTuple[0],".",idTuple[1],".",idTuple[2],".",idTuple[3])
        allPackets = True
    else:
        if totalOfPackets > 0:
            print("Recebidos", numberOfPackets, "pacotes de um total de ", totalOfPackets,"pacotes da mensagem",idTuple[4], "vinda de", idTuple[0],".",idTuple[1],".",idTuple[2],".",idTuple[3])
        else:
            print("Recebidos", numberOfPackets, "pacotes da mensagem",idTuple[4], "vinda de", idTuple[0],".",idTuple[1],".",idTuple[2],".",idTuple[3])

    return allPackets

def appendPackets(idTuple):
    offset = 0
    done = False
    appendedMsg = bytearray()


    while not done:
        #sequencialmente, vai juntando os pacotes da mesma mensagem, comecando com offset 0
            #e aumentando de 185(offsets sao multiplos de 185 com mtu 1500)
        tuple = (idTuple[0], idTuple[1], idTuple[2], idTuple[3], idTuple[4], offset)

        #e retirado o cabecalho para juntar as mensagens
        packet = receivedPackages[tuple][20:]

        #junta o pacote atual na mensagem completa e passa para o proximo pacote
        appendedMsg = appendedMsg + packet
        offset = offset + 185

        #se chegar no ultimo pacote, nao precisa mais juntar nenhum pacote
        packetFlag = receivedPackages[tuple][6] & 0b11100000
        #nao e mais necessario armazenar o pacote da mensagem
        del receivedPackages[tuple]
        if packetFlag == 0:
            print("Mensagem desfragmentada!")
            done = True

    #print(appendedMsg)
    return appendedMsg

if __name__ == '__main__':

    #INICIALIZACAO DA ETAPA 3
    idTuple = (0, 0, 0, 0, 0, 0)
    discard = asyncio.get_event_loop().call_later(10, discard_packet, idTuple)

    # Ver http://man7.org/linux/man-pages/man7/packet.7.html
    fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
    fd.bind((if_name, 0))

    loop = asyncio.get_event_loop()
    loop.add_reader(fd, raw_recv, fd)
    loop.run_forever()
