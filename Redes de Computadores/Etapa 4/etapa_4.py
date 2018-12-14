import socket
import asyncio
import struct


ETH_P_ALL = 0x0003
ETH_P_IP  = 0x0800


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


#PARAMETROS DA ETAPA 3

receivedPackages = {}

#inicializacao da variavel para syncio.get_event_loop().call_later()
discard = None 


def ip_addr_to_bytes(addr):
    return bytes(map(int, addr.split('.')))


def mac_addr_to_bytes(addr):
    return bytes(int('0x'+s, 16) for s in addr.split(':'))


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


def send_ping(fd):
    print('enviando ping')
    # Exemplo de pacote ping (ICMP echo request) com payload grande
    msg = bytearray(b"\x08\x00\x00\x00" + 5*b"\xba\xdc\x0f\xfe")
    msg[2:4] = struct.pack('!H', calc_checksum(msg))

    send_ip(fd, msg, ICMP)

    asyncio.get_event_loop().call_later(1, send_ping, fd)


def raw_recv(fd):
    frame = fd.recv(12000)
    
    print("\n =========================== \n")

    #Verifica MAC e Protocol
    if verify_MAC(frame) and verify_protocol(frame):
        print('recebido quadro de %d bytes' % len(frame))
        print(repr(frame))
        #Obtem o Datagram
        datagram = frame[14:]
        defragMSG = defrag(datagram)
    else:
        print("Nao passou na verificacao")


def verify_MAC(frame):
    print("****Verificando MAC addr****")

    dest_mac_bytes = frame[0:6]
    src_mac_bytes  = mac_addr_to_bytes(src_mac)

    print("MAC de destino : ", ':'.join('%02x'%x for x in dest_mac_bytes))
    print("Meu MAC : ", ':'.join('%02x'%x for x in src_mac_bytes))

    if dest_mac_bytes == src_mac_bytes:
        return True
    else:
        return False

def verify_protocol(frame):
    print("****Verficando o protocolo****")
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

#------------------------------------------FUNCOES DA ETAPA 3----------------------------------------------------------------
def discard_packet(idTuple):

    print("******************DESCARTANDO ", idTuple, " POR TIMEOUT*****************\n")
    for tuple in receivedPackages:
       if idTuple[0] == tuple[0] and idTuple[1] == tuple[1] and idTuple[2] == tuple[2] and idTuple[3] == tuple[3] and idTuple[4] == tuple[4]:
           del receivedPackages[tuple]

def defrag(packet):

    print("***Entrando no Processamento do Frame - Etapa 3***")

    global discard
    global lastTuple

    appendedMsg = packet

    packetFlag = packet[6] & 0b11100000

    #o flag de fragmentacao fica 32 se ha mais fragamentos ou 0 para o ultimo pacote de fragmentacao.
        #64 se nao precisa de fragmentacao
    if packetFlag <= 32:
        #Chegou um pacote, cancela o timeout
        discard.cancel()

        #o id da mensagem ocupa dois bytes do cabecalho, para ter o numero de id e 
        #necessario calcular o numero desses 2 bytes
        id = packet[4]*256 + packet[5]

        #assim como o id, o offset ocupa mais de um byte, para isso pega o nibble 
        #menos significativo e calcula junto com o segundo byte
        offset = (packet[6] & 0b00011111)*256 + packet[7]

        #os byte 12, 13, 14 e 15 sao o endereco de destino da mensagem, para 
        #identificar de qual mensagem pertence o fragamentos
        #usa o endereco, o id e o offset(para verificar qual parte da mensagem e)
        idTuple = (packet[12], packet[13], packet[14], packet[15], id, offset)
        lastTuple = idTuple

        #se o pacote nao e repetido, adiciona na lista de pacotes recebidos
        if not idTuple in receivedPackages:
            receivedPackages[idTuple] = packet

        #Inicia a espera por outro pacote
        discard = asyncio.get_event_loop().call_later(3, discard_packet, idTuple)

        #checa se todos os pacotes da mensagem chegaram, se chegaram desfragmente a mensagem
        if checkAllPackets(idTuple):
            appendedMsg = appendPackets(idTuple)

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
    asyncio.get_event_loop().call_later(1, send_ping, fd)
    loop.run_forever()
