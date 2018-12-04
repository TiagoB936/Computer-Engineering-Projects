from manipulador_da_tabela import ManipuladorDaTabela
from decisor import Decisor
from PID import PID
import time
import numpy as np

#Seleciona qual metodo de controle sera utilizado
# 0 - Nenhum controle
# 1 - PID Simples
# 2 - PID Adaptativo
# 3 - Fuzzy
seletorControle = 2

#Criacao dos objetos da classe
decisor = Decisor()
manipulador = ManipuladorDaTabela()
PID = PID()

#Parametros inicias
qnt_leituras = 0 #quantidade de amostras
num_amostras = decisor.get_amostra() #numero de amostras
decisor.set_limite_desvio(3.5) 
decisor.set_limite_media(1) 
saida_visao = 5.0 # saida de angulo visao computacional
sample_time  = 0.0
PID.setSetPoint(1.0)
output = 0.0
kp = 1.0
ki = 0.5
kd = 0.2
nome_da_tabela = "tabela_de_sintonia.csv"

#feedback inicial como numero aleatorio entre -6 e 6
#isso vai simular o erro de angulo da visao
saida_visao = np.random.randint(-6,6)
PID.setSampleTime(1.0)

#Calcula um PID simples com os valores kp, ki e kd
#e retorna o ganho
def PIDSimples(kp, ki, kd):

	#Simula a leitura da visao	
	saida_visao = np.random.randint(-6,6)

	PID.setKp(float(kp))
	PID.setKi(float(ki))
	PID.setKd(float(kd))
		
	#Calcula o output
	PID.update(saida_visao)

	#pega o output
	output = PID.getOutput()

	return output

#Calcula o PID Adaptativo com base numa tabela de 
#sintonia e retorna o ganhos	
def PIDAdaptativo(nome_da_tabela):
	
	global qnt_leituras

	#Simula a leitura da visao	
	saida_visao = np.random.randint(-6,6)

	sample_time = PID.getSampleTime()
	time.sleep(sample_time)
	
	#adiciona o erro no decisor
	decisor.add_erro(saida_visao) 
	
	#soma uma leitura
	qnt_leituras = qnt_leituras + 1
	
	#caso tenha o numero de amostras, deve verificar
	#a performance
	if qnt_leituras >= num_amostras:
		qnt_leituras = 0
	
		#calcula o novo indice se precisar
		index = decisor.computa_index()
		
		#obtem as constantes e atribui ao PID Simples
		manipulador.le_tabela(nome_da_tabela)
		constantes = decisor.get_constantes(manipulador, index)
		PID.setKp(float(constantes[0]))
		PID.setKi(float(constantes[1]))
		PID.setKd(float(constantes[2]))

	#Calcula o output
	PID.update(saida_visao)

	#pega o output
	output = PID.getOutput()

	return output
	
#Calcula o ganho com um Controle Fuzzy
def ControleFuzzy():
	print("Ainda nao implementado")
	return -1

def main():

	#Saida do controle
	output = 0.0
	
	#Se for 0 nao roda nenhum controle
	while seletorControle!=0:
		# TODO: Ler o tipo de controle pela interface
		if seletorControle == 1:
			print("Executando o PID Simples")
			# TODO: Ler Kp, Ki e Kd da interface
			# TODO: Ler sample time
			# TODO: Ler SetPoint
			output = PIDSimples(kp, ki, kd)
		if seletorControle == 2:
			print("Executando o PID Adaptativo")
			# TODO: Ler o nome da tabela da interface
			# TODO: Ler numero de amostras
			# TODO: Ler o sample time
			# TODO: Ler o limite de desvio padroa
			# TODO: Ler o limite da media
			# TODO: Ler SetPoint
			# TODO: Ler indice inicial da tabela
			output = PIDAdaptativo(nome_da_tabela)
		if seletorControle == 3:
			print("Executando o Controle Fuzzy")
			output = ControleFuzzy()	
		print(output)		
	return
	
if __name__ == "__main__":
	main()
