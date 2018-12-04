from manipulador_da_tabela import ManipuladorDaTabela
from decisor import Decisor
from PID import PID
import time
import numpy as np

decisor = Decisor()
manipulador = ManipuladorDaTabela()
PID = PID()

manipulador.criar_tabela()
manipulador.le_tabela()

manipulador.add_parametros(10.0, 0.05, 0.2)
manipulador.add_parametros(8.0, 0.1, 0.1)
manipulador.add_parametros(11, 0.2, 0.3)
manipulador.add_parametros(9.0, 0.8, 0.3)

manipulador.escreve_tabela()
