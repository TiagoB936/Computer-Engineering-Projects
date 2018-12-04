from manipulador_da_tabela import ManipuladorDaTabela
from decisor import Decisor
from PID import PID
import time
import numpy as np

decisor = Decisor()
manipulador = ManipuladorDaTabela()
PID = PID()

qnt_leituras = 0 #quantas leituras da visao
num_amostras = decisor.get_amostra() #numero de amostras
e = 0 #erro
decisor.set_limite_desvio(1) 
decisor.set_limite_media(1) 
get_erro_angulo_visao = 5.0 #erro inicial da visao
sample_time  = 0.0
tau = 5 
PID.setSetPoint(1.0)
feedback = 0.0
output = 0.0
last_output = 0.0
last_feedback = 0.0

#feedback inicial como numero aleatorio entre -6 e 6
#isso vai simular o erro de angulo da visao
feedback = np.random.randint(-6,6)
PID.setSampleTime(1.0)

while(1): 

	last_output = output
	
	sample_time = PID.getSampleTime()
	time.sleep(sample_time)
	
	#adiciona o erro no decisor
	decisor.add_erro(feedback) 
	
	#soma uma leitura
	qnt_leituras = qnt_leituras + 1
	
	#caso tenha o numero de amostras, deve verificar
	#a performance
	if qnt_leituras >= num_amostras:
		qnt_leituras = 0
	
		#calcula o novo indice se precisar
		index = decisor.computa_index()
		
		#obtem as constantes e atribui ao PID Simples
		manipulador.le_tabela()
		constantes = decisor.get_constantes(manipulador, index)
		PID.setKp(float(constantes[0]))
		PID.setKi(float(constantes[1]))
		PID.setKd(float(constantes[2]))

	#coloca o feedback da planta + um valor aleatorio da visao no PID
	PID.update(feedback + np.random.randint(-6,6))
	#pega o output
	output = PID.getOutput()
	
	#Exibe os resultados
	print("-----------------------------------------------------")
	print("SETPOINT: " + str(PID.SetPoint))
	print("KP: " + str(PID.getKp()))
	print("KI: " + str(PID.getKi()))
	print("KD: " + str(PID.getKd()))
	print("MEDIA: " + str(decisor.get_media()) + " / LIMITE MEDIA: " + str(decisor.get_limite_media()))
	print("DESVIO: " + str(decisor.get_desvio_padrao()) + " / LIMITE DESVIO: " + str(decisor.get_limite_desvio()))
	print("OUTPUT DO PID: " + str(output))

	# Atualizacao da planta
    # Planta de primeira ordem discretizada pelo metodo de Tustin
	last_feedback = feedback
	feedback = last_feedback*((2*tau - sample_time)/(2*tau + sample_time))+output*((sample_time)/(2*tau + sample_time))+last_output*((sample_time)/(2*tau + sample_time))
	print ("FEEDBACK: " + str(feedback))

