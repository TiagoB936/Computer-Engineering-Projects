import numpy as np

class Decisor:
	erros = []
	amostra = 10
	constantes = []
	idx = 0
	#valores iniciais. O usuario deve selecionar
	#o valor que melhor se encaixa
	limite_media = 5
	limite_desvio = 0
	media = 0
	desvio_padrao = 0

	#Adiciona valores de erro no vetor de erros
	def add_erro(self, erro):
		#se exisitir mais que o numero de amostras de erros
		#vai remover o ultimo inserido antes de adicionar o novo
		if len(self.erros) >= self.amostra:
			self.erros.pop(0)
		self.erros.append(erro)
	
	def set_amostra(self, amostra):
		self.amostra = amostra

	def set_limite_media(self, limite):
		self.limite_media = limite

	def set_limite_desvio(self, limite):
		self.limite_desvio = limite

	def set_index(self, idx):
		self.idx = idx

	def get_index(self):
		return self.idx
	
	def get_amostra(self):
		return self.amostra

	def get_media(self):
		return self.media

	def get_desvio_padrao(self):
		return self.desvio_padrao

	def get_limite_media(self):
		return self.limite_media
	
	def get_limite_desvio(self):
		return self.limite_desvio
	
	def set_constantes(self,kp, ki, kd):
		self.constantes[:] = []
		self.constantes.append(kp)
		self.constantes.append(ki)
		self.constantes.append(kd)
	
	#Usa media e desvio padrao para calcular o indice da Tabela
	def computa_index(self):
		#calcula a media
		self.media = np.mean(self.erros)
		#calcula o desvio padrao
		self.desvio_padrao = np.std(self.erros)
		#calcula o valor absoluto da media
		media_abs = abs(self.media)
		
		#Estamos realizando uma busca sucessiva (rampa).
		#Existe a alternativa de busca de aproximacao sucessiva (ponto medio)
		#verifica as condicoes e edita o indice
		if media_abs < self.limite_media and self.desvio_padrao > self.limite_desvio:		
			self.idx = self.idx - 1
		elif media_abs > self.limite_media and self.desvio_padrao < self.limite_desvio: 
			self.idx = self.idx + 1

		return self.idx

	#usa o manipulador de tabelas para a acessar as contantes
	def get_constantes(self, manipulador, idx):
		self.constantes = manipulador.get_constantes(idx)
		#primeira linha e invalida, entao pega a proxima
		if self.constantes[0] == 0.0: 
			self.idx = idx + 1
			self.constantes = manipulador.get_constantes(self.idx)
		#ultima linha e invalida, entao pega a anterior
		if self.constantes[0] == float('Inf'):
			self.idx = idx - 1
			self.constantes = manipulador.get_constantes(self.idx)
		return self.constantes

