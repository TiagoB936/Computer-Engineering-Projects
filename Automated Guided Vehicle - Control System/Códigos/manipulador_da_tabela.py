import csv
from operator import itemgetter

#A tabela esta sendo ordenada pelo Ki, pois a agressividade da
#correcao do angulo esta relacionada a somatoria dos erros acumulado
class ManipuladorDaTabela:
	
	tabela = list()
	nome_da_tabela = "tabela_de_sintonia.csv"

	#Cria um arquivo .csv com o nome da tabela especificado
	def criar_tabela(self):
		f = open(self.nome_da_tabela, "w+")
		f.close()

	#Abre o arquivo especificado em nome_da_tabela e le seu
	#conteudo numa lista
	def le_tabela(self):
		#abre um indicador para o csv
		reader = csv.reader(open(self.nome_da_tabela))
		#tranforma os elementos da tabela em uma lista
		tabela_str = list(reader)

		#Configura o primeiro e o ultimo elementos da tabela, que devem
		#ser como especificados a seguir
		if len(tabela_str) == 0:
			self.tabela.append([0,0,0])
			self.tabela.append([float('Inf'),float('Inf'),float('Inf')])
		
		for i in range(len(tabela_str)):
			row = list()
			for j in range(len(tabela_str[i])):
				row.append(float(tabela_str[i][j]))
			self.tabela.append(row)

	#Escreve dados na tabela especificada em nome_da_tabela
	def escreve_tabela(self):
		#Nao fizemos um sistema de desempate, para o caso onde tenham
		#dois ou mais Kis iguais na tabela
		self.tabela.sort(key=itemgetter(1), reverse=False)
		writer = csv.writer(open(self.nome_da_tabela, "w", newline = ''))
		writer.writerows(self.tabela)
	
	def limpa_tabela(self):
		f = open(self.nome_da_tabela, "w+")
		f.close()
		
	def set_kp(self, kp, idx):
		#Nao permite tentar acesso a posicao inexistente
		if idx >= len(self.tabela):
			print("Nao existe elemento nesta posicao da tabela")
		#Nao permite a edicao do primeiro e ultimo elementos pois sao elementos de controle
		elif self.tabela[idx][0] != 0.0 and self.tabela[idx][0] != float('Inf'):
			#edita a o parametro
			self.tabela[idx][0] = kp
		else:
			print("Voce esta tentando editar uma posicao da tabela que nao existe!")
		
	def set_ki(self, ki, idx):
		if idx >= len(self.tabela):
			print("Nao existe elemento nesta posicao da tabela")
		elif self.tabela[idx][0] != 0.0 and self.tabela[idx][0] != float('Inf'):
			#edita a o parametro
			self.tabela[idx][1] = ki
		else:
			print("Voce esta tentando editar uma posicao da tabela que nao existe!")

	def set_kd(self, kd, idx):
		if idx >= len(self.tabela):
			print("Nao existe elemento nesta posicao da tabela")
		elif self.tabela[idx][0] != 0.0 and self.tabela[idx][0] != float('Inf'):
			#edita a o parametro
			self.tabela[idx][2] = kd
		else:
			print("Voce esta tentando editar uma posicao da tabela que nao existe!")

	def set_parametros(self, kp, ki, kd, idx):
		if idx >= len(self.tabela):
			print("Nao existe elemento nesta posicao da tabela")
		elif self.tabela[idx][0] != 0.0 and self.tabela[idx][0] != float('Inf'):
                        #edita a o parametro
			self.tabela[idx][0] = kp
			self.tabela[idx][1] = ki
			self.tabela[idx][2] = kd
		else:
			print("Voce esta tentando editar uma posicao da tabela que nao existe!")

	def set_nome_tabela(nome_da_tabela):
		self.nome_da_tabela = nome_da_tabela
		
	def add_parametros(self, kp, ki, kd):
		self.tabela.append([kp, ki, kd])

	def get_kp(self, idx):
		#le o elemento
		kp = self.tabela[idx][0]
		return  kp

	def get_ki(self, idx):
		ki = self.tabela[idx][1]
		return  ki

	def get_kd(self, idx):
		kd = self.tabela[idx][2]
		return kd

	def get_tamanho_tabela(self):
		print(len(self.tabela))
		return len(self.tabela)

	def get_nome_tabela():
		return self.nome_da_tabela

	#sempre vai recalibrar o kp, ki e kd. Nunca um individualmente
	#se quisermos verificar individualmente, devemos ver outros parametros
	#que sao o erro, overshooting, etc, para cada entrada degrau, comparando
	#sempre com o anterior
	def get_constantes(self, idx):
		#cria uma lista de constantes
		constantes=[]
		#adiciona os parametros na lista
		constantes.append(self.get_kp(idx))
		constantes.append(self.get_ki(idx))
		constantes.append(self.get_kd(idx))
		return constantes
