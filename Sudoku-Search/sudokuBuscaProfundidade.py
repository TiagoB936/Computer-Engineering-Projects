#|------------------------------------------------------#
#|Trabalho de buscas - Inteligência artificial          #
#|Grupo:                                                #
#|Leonardo Utida Alcantara 628182                       #
#|Leonardo Tavares Oliveira 628174                      #
#|Tiago Bachiega de Almeida 628247                      #
#|------------------------------------------------------#
#|Resolucao de um jogo Sudoku utilizando a busca em     #
#|profundidade (não informada)                          #
#|------------------------------------------------------#


# A ideia do algoritmo é que a cada iteração ele procura por um espaço vazio (representado por valores de 0)
# Essa busca é sempre feita da esquerda para a direita e de cima para baixo no tabuleiro.
# Após um valor ser encontrado, o algoritmo entra em um loop for que testa todos os 9 possíveis valores para
# aquele espaço, sempre verificando se aquela jogada é possível. 
#
# Caso o a jogada (combinação de valor e posição) seja possível, o algoritmo atribui o novo valor para a 
# posição e chama a função de resolver o  sudoku recursivamente no novo tabuleiro.
# Quando uma jogada não pode ser feita, o algoritmo tenta o próximo valor possível para aquela posição. 
# Caso nenhum valor seja possível, o algoritmo retorna falso para a função acima na recusão indicando que
# o caminho escolhido não leva ao resultado final e este tenta outro valor.
# Caso o valor Falso retorne, para todas as oções, até a primeira chamada da função que resolve o jogo,
# o algoritmo final retorna falso indicando que não foi possível resolver o jogo.


from os import system, name
from time import sleep

#DEBUG
debug = False 

# Conta o número de iterações até ser resolvido o jogo
numIter = 0

# Funcao de limpar tela
def limpaTela(): 
    # Windows 
    if name == 'nt': 
        _ = system('cls') 
    # mac e linux 
    else: 
        _ = system('clear') 

# Função que recebe um tabuleior na forma de listas e printa na tela de um jeito mais fácil de ver
def printaTabuleiro(tabuleiro):
    print("+" + "---+"*9)
    for i, row in enumerate(tabuleiro):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)

# Função que acha a próxima possição vazia do tabuleiro para realizar a próxima jogada
def achaProxPosVazia(tabuleiro):
    for i in range(0,9):
        for j in range(0,9):
            if tabuleiro[i][j] == 0:
                return i,j
    return -1,-1

# Função que verifica se a jogada é possivel
# Verifica 3 condições:
### Se não há o valor na linha
### Se não há o valor na coluna
### Se não há o valor na seção (quadrado)
def valorLocalValido(tabuleiro, row, col, val):
    # Verifica se não há o valor da jogada na linha
    for j in range(9):
        if tabuleiro[row][j] == val:
            return False
    # Verifica se não há o valor da jogada na coluna
    for i in range(9):
        if tabuleiro[i][col] == val:
            return False

    # Verifica se não há o valor da jogada na seção
    secLinInicial = (row//3) * 3
    secColInicial = (col//3) * 3
    for i in range(secLinInicial, secLinInicial+3):
        for j in range(secColInicial, secColInicial+3):
            if tabuleiro[i][j] == val:
                return False
    # Se nao encontrou nenhum problema retorna verdadeiro
    return True

# Função se resuloção do jogo que é chamada recursivamente
# Recebe o tabuleiro e o tempo de espera para melhor visualização
def resolverSudoku(tabuleiro, tempoEspera):

    #variavel global para o número de iterações
    global numIter

    #Mais uma iteração
    numIter = numIter + 1 

    limpaTela()
    printaTabuleiro(tabuleiro)
    # Espera 0.5 segundos para a próxima jogada para melhor visualização
    sleep(tempoEspera)

    row,col = achaProxPosVazia(tabuleiro)
    if row == -1 or col == -1: #nao ha mais valores 0, o jogo foi concluído
        return True

    #Testa todos os 9 possíveis valores começando em 0
    for val in range(1,10):
        # verifica se a jogada é valida
        if(valorLocalValido(tabuleiro, row, col, val)):
            # Se a jogada é valida, atualiza o tabuleiro e resolve o novo jogo
            tabuleiro[row][col] = val
            if(resolverSudoku(tabuleiro, tempoEspera)):
                return True
            # Se um falso foi retornado desfaz a última jogada e tenta o proximo valor
            tabuleiro[row][col] = 0
    # Se nenhum valor foi encontrado, retorna falso, indicando que não eh possivel resolver
    return False

    
muitoFacil = [
[1, 0, 0, 5, 0, 9, 6, 7, 0],
[4, 0, 2, 8, 7, 0, 0, 1, 9],
[9, 6, 7, 1, 4, 3, 2, 8, 5],
[2, 0, 4, 9, 0, 0, 0, 0, 0],
[5, 0, 6, 0, 0, 0, 0, 0, 8],
[0, 0, 0, 0, 1, 0, 4, 2, 0],
[0, 0, 0, 3, 6, 2, 7, 4, 0],
[6, 4, 0, 0, 0, 1, 0, 5, 0],
[0, 2, 1, 4, 0, 8, 9, 3, 6],
]

facil = [
[1, 2, 9, 0, 6, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 0, 0, 0, 9],
[0, 0, 0, 3, 5, 0, 0, 0, 8],
[0, 0, 0, 8, 0, 3, 9, 0, 0],
[3, 0, 1, 0, 0, 0, 5, 0, 2],
[0, 0, 6, 1, 0, 5, 0, 0, 0],
[4, 0, 0, 0, 7, 6, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0],
[9, 0, 0, 0, 8, 0, 1, 3, 4],
]

medio = [
[6, 0, 1, 0, 0, 0, 5, 0, 8],
[0, 0, 0, 0, 8, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 2, 0, 0, 0],
[2, 0, 8, 1, 0, 4, 6, 0, 3],
[1, 0, 0, 3, 0, 7, 0, 0, 4],
[0, 0, 3, 0, 0, 0, 7, 0, 0],
[7, 6, 0, 0, 0, 0, 0, 1, 2],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 6, 0, 8, 0, 4, 0],
]

dificil = [
[0, 0, 7, 5, 0, 1, 9, 0, 0],
[0, 0, 8, 0, 6, 0, 4, 0, 0],
[0, 5, 0, 8, 0, 4, 0, 7, 0],
[0, 0, 2, 0, 7, 0, 3, 0, 0],
[4, 0, 0, 0, 8, 0, 0, 0, 9],
[0, 3, 0, 0, 1, 0, 0, 6, 0],
[1, 9, 0, 0, 0, 0, 0, 5, 4],
[0, 7, 0, 0, 0, 0, 0, 3, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
]

muitoDificil = [
[4, 0, 0, 0, 0, 0, 0, 0, 7],
[2, 0, 0, 0, 1, 0, 0, 0, 4],
[0, 1, 0, 0, 0, 0, 0, 5, 0],
[5, 0, 1, 0, 4, 0, 7, 0, 6],
[0, 3, 0, 1, 0, 8, 0, 4, 0],
[0, 0, 0, 6, 0, 3, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 4, 0, 0],
[7, 0, 0, 0, 8, 0, 0, 0, 9],
[0, 5, 0, 0, 2, 0, 0, 7, 0],
]

#VARIAVEIS DE DEBUG
if (debug):
	sleepTime = 0.0
else:
	sleepTime = 0.5

meuSudoku = []

# Opcao do usuario
opcao = 0

limpaTela()

# Menu inicial
print("**********SUDOKU IA**********")
print("\n\nSelecione o tipo de jogo:")
print("1 - Rodar exemplo Muito Fácil")
print("2 - Rodar exemplo Fácil")
print("3 - Rodar exemplo Médio")
print("4 - Rodar exemplo Difícil")
print("5 - Rodar exemplo Muito Difícil")
print("6 - Inserir um Sudoku")

#Le opção
opcao = int(input())

#Trata cada opção
if opcao == 1:
    print(resolverSudoku(muitoFacil, sleepTime), "\n", "Número de iterações: ", numIter)
elif opcao == 2:
    print(resolverSudoku(facil, sleepTime), "\n", "Número de iterações: ", numIter)
elif opcao == 3:
    print(resolverSudoku(medio, sleepTime), "\n", "Número de iterações: ", numIter)
elif opcao == 4:
    print(resolverSudoku(dificil, sleepTime), "\n", "Número de iterações: ", numIter)
elif opcao == 5:
    print(resolverSudoku(muitoDificil, sleepTime), "\n", "Número de iterações: ", numIter)
elif opcao == 6:
    limpaTela()
    print("Digite seu Sudoku, os elementos devem ser números de 0 a 9, sendo 0 uma casa vazia\n")

    # Lê os inputs do usuários
    for i in range(0, 9):
        elementos = list(map(int, input().split()))

        #Condições do sudoku
        while(len(elementos) != 9):
            print("Cada fileira deve ter 9 elementos")
            elementos = list(map(int, input().split()))
        while(i > 9 or i < 0 for i in elementos):
            print("Os elementos devem ser de 0 a 9")
            elementos = list(map(int, input().split()))
        meuSudoku.append(elementos)

    print(resolverSudoku(meuSudoku, sleepTime), "\n", "Número de iterações: ", numIter)