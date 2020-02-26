# Alunos:
# Tiago Bachiega de Almeida RA: 628247
# Victor Tavares RA: 628140

import socket, settings

#O arquivo a seguir contem as classes TupleSpace e Linda. Idealmente, o computador
# onde estara sendo rodado o servidor devera ter apenas a class TupleSpace e os 
# computadores onde estao sendo rodados os clientes deverao ter apenas acesso
# a classe Linda. Coloquei ambos no mesmo arquivo apenas para simplificar a
# organizacao.


#Tuple Space
# Esta classe armazena os topics existentes e tambem possui uma lista
# que relaciona as mensagens existentes com quem as mandous
class TupleSpace():

    def __init__(self, topic):
        self.topic = topic #Topic
        self.names_messages = [] 

# Interface Linda
# Usada pelo cliente para atuar o Tuple Space
class Linda(object):
    # Construtur
    # Recebe o nome do cliente e o topico de interesse
    def __init__(self, name, topic):
        super(Linda, self).__init__()
        self.name = name
        self.topic = topic
        # Obtem o host do cliente do arquivo settings.py
        self.host = settings.host_client 
        # Obtem a porta do cliente do arquivo settings.py
        self.port = settings.port
        # Inicializa a conexao cliente-servidor
        self.client_socket = self.connect()

    # Inicializa a conexao cliente servidor para o cliente que esta usando
    # um objeto Linda
    def connect(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Abre o socket
        client_socket.connect((self.host, self.port)) # Conecta com o host e porta
        message = self.name + ',' + self.topic # Mensagem inicial informando nome e topico
        client_socket.send(message) # Envia a mensagem inicial
        return client_socket # Retorna o socket criado

    # Finaliza a conexao fechando o socket
    def quit(self):
        self.client_socket.close()

    # Universe Out do Linda
    # Envia uma mensagem para o tuple space
    # Recebe como parametro a mensagem a ser enviada
    def universe_out(self, message):
        # Monta a mensagem da seguinte forma <nome do comando:><nome>,<topico>,<mensagem>
        message = "universe_out: "+ self.name + ',' + self.topic + ',' + message 
        self.client_socket.send(message) # Envia para o servidor

    # Universe Rd do Linda
    # Le todas as menagens de do topico, ou seja, le todo o Tuple Space
    def universe_rd(self):
        # Mensagem de requisicao do Tuple Space especificando o topico
        message = "universe_rd:"+self.topic
        # Envia a mensagem
        self.client_socket.send(message)
        # Espera a resposta do servidor
        answer = self.client_socket.recv(4096)
        # Exibe a resposta
        print(answer)

    # Linda Blog In
    # Le a ultima mensagem sobre o topico e a remove do Tuple Space
    def blog_in(self):
        # Mensagem de requisicao da ultima mensagem do Tuple Space do topico
        message = "blog_in:"+self.topic
        # Envia a mensagem para o servidor
        self.client_socket.send(message)
        # Recebe a ultima mensagem, uma tupla
        rd_tuple = self.client_socket.recv(4096)
        # Exibe a mensagem
        print(rd_tuple)
