# Alunos:
# Tiago Bachiega de Almeida RA: 628247
# Victor Tavares RA: 628140

import socket, settings,select

# Servidor usa somento o TupleSpace
from linda import TupleSpace

# Lista de conexoes
connected_list = []
# Dicionario com as Tuple Spaces de topicos
list_of_topics = {}

# Realiza a conexao do socket servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
server_socket.bind((settings.host_server, settings.port))

# Recebe a conexao de um nome cliente e atualiza o Tuple Space com ele
def connect():
	# Aceita a conexao
	sockfd, addr = server_socket.accept()

	# Obtem um dado de formado <nome do cliente>,<topico>
	data =str(sockfd.recv(4096))
	# Separa nome e topico pelo separador virgula
	name, topic = data.split(',')	

	print(name + " joined for " + topic)

	# Adiciona na lista de conectados
	connected_list.append(sockfd)

	# Caso o topico nao exista no dicionario, adiciona essa Tuple Space
	if topic not in list_of_topics.keys():
		list_of_topics[topic] = TupleSpace(topic)

# Trata o recebimetno de mensagens dos clientes
def handle_incoming_msg(sock):
	# Recebe a mensagem do cliente
	data = sock.recv(4096)

	# Se existir o identificador de comando universe_out:
	if 'universe_out' in data:
		print("universe_out DOING")
		# Obtem o nome, topico e mensagem atraves da manipulacao dos separadores
		name, topic, message = (data.split(':')[1]).split(',')
		# Adiciona esta mensagem no Tuple Space atraves do dicionario
		# de Tuple Spaces. A mensagem ser adicionada no fim da lista
		# names_messages como uma tupla contendo o nome de quem enviou
		# e a mensagem
		list_of_topics[topic].names_messages.append((name, message))
		print("universe_out DONE")

	# Se existir o comando universe_rd
	if 'universe_rd' in data:
		print("universe_rd DOING") 
		# Obtem a informacao do topico a partir do dado
		topic = data.split(':')[1]

		#print(list_of_topics[topic].names_messages)
		
		# Aqui vamos obter todas as mensagens do Tuple Space sobre
		# um determinado topico.
		# Vamos montar uma mensagem da seguinte forma
		# <nome>:<mensagem>\n
		# <name>:<mensagem>\n
		# ....
		# Isso e feito manipulando-se a lista names_messages
		# dos Tuple Space que estar armazenados em list_of_topics,
		# para um determinado topico
		tuple_msgs = ""

		if len(list_of_topics[topic].names_messages) == 0:
			tuple_msgs = "No message about that topic\n"
		else:
			for i in range(len(list_of_topics[topic].names_messages)):
				name = list_of_topics[topic].names_messages[i][0]
				msg = list_of_topics[topic].names_messages[i][1]
				tuple_msgs = tuple_msgs + name + ": " + msg + "\n"

		# Envia todas as mensagens para o cliente
		sock.send(tuple_msgs)
		print("universe_rd DONE")

	# Se o comando for blog_in
	if 'blog_in' in data:
		print("blog_in DOING")
		# Obtem a informacao do topico da mensagem recebida
		topic = data.split(':')[1]
		# Remove o ultimo elemento das mensagens do Tuple Space
		# e obtem seu valor se houver algo na lista
		if len(list_of_topics[topic].names_messages) > 0:
			msg = list_of_topics[topic].names_messages.pop()
			# Envia a partir da mensagem obtida o nome de quem enviou
			# e a mensagem em si para o cliente
			sock.send(msg[0] + ': ' + msg[1])
		else:
			sock.send("No message about that topic")
		print("blog_in DONE")



def main():
	# Recebe ate 10 clientes
	server_socket.listen(10)
	# Para cada conexao, adiciona na lista de conectados
	connected_list.append(server_socket)

	print("Servidor Inicializado")

	while True:
		# Utiliza o select para obter as listas de sockets conectados que
		# podemos ler, podemos escrever e que estao com erros
		readable,writable,exceptional = select.select(connected_list,[],[])

		# Para todos os sockets que podemos escrever
		for sock in readable:
	            # Caso este socket seja um novo cliente
	            # tratar a conexao
	            if sock == server_socket:
	                connect()

	            # Caso seja uma mensagem de algum cliente
	            # tratar o recebimento da mensagem
	            else:
	                handle_incoming_msg(sock)

	server_socket.close()

if __name__ == '__main__':
	main()
