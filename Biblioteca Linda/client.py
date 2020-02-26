# Alunos:
# Tiago Bachiega de Almeida RA: 628247
# Victor Tavares RA: 628140

import socket, settings, os

# Cliente usa o Linda de interface
from linda import Linda

# Manipula o input do usuario usando o objeto linda
def handle_user_input(linda, user_input):

	# Se escolheu Write
	if user_input == "Write":
		# Le a entrada do usuario
		msg = raw_input("Message: ")
		# Chama universe_out com a mensagem de entrada como parametro
		linda.universe_out(msg)

	# Se escolheu Read
	elif user_input == "Read":
		print("Reading....")
		# Chama universe_rd para ler todas as mensagem do Tuple Space sobre o topico
		linda.universe_rd()
		_ = raw_input("Press Enter to continue...")

	# Se escolheu Delete
	elif user_input == "Delete":
		print("Reading and deleting last tuple....")
		# Chama blog_in para ler a ultima mensagem do Tuple Space sobre o topico
		# e remove-la do Tuple Space
		linda.blog_in()
		_ = raw_input("Press Enter to continue...")

	# Se escolheu Quit
	elif user_input == "Quit":
		# Chama quit e encerra a conexao
		linda.quit()


def main():
	
	# Obtem o nome e topico de interesse do cliente
	name = raw_input("Name: ")
	topic = raw_input("Topic: ")

	# Inicializa um objeto linda que tem a conexao cliente-servidor
	linda = Linda(name, topic)

	# Loop do cliente
	quit = False
	while not quit:
		os.system('clear')

		# Obtem o input do usuario, informando se ele quer escrever, ler, deletar ou sair
		# Write - Escreve uma mensagem no Tuple Space sobre o topico
		# Read - Le todo o Tuple Space sobre o topico
		# Delete - Le a ultima mensagem do Tuple Space sobre o topico e a deleta
		# Quit - Encerra a operacao 
		user_input = raw_input("Commands:\n >>Write (Adds a new tuple)\n >>Read (Reads all the tuples of topic)\n >>Delete (Reads and deletes last tuple)\n >>Quit\n")

		if user_input == "Quit":
			quit = True

		# Manipula o input do usuario usando o objeto linda	
		handle_user_input(linda, user_input)

if __name__ == '__main__':
	main()

