# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Crie um pequeno jogo do tipo Campo Minado. Para isto siga as atividades abaixo:              ******
# ******             1) Crie uma matriz (10 x 10) contendo numeros 0.                                             ******
# ******             2) Popule a matriz c/ 10 bombas colocando o numero 200 em 10 posições aleatórias(200 = bomba)******
# ******             3) Faça dois loops para iterar sobre toda a matriz e modifique as celulas para conter a      ******
# ******                quantidade de bombas que estão em sua fronteira                                           ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 17/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import randint

def montar_matriz():
    for x in range(10):
        tabuleiro.append([])
        for y in range(10):
            tabuleiro[x].append(0)

def imprimir_tabuleiro(matriz):
    linha = 0
    print('     A1 -  A2 -  A3 -  A4 -  A5 -  A6 -  A7 -  A8 -  A9 -  A10')
    for row in matriz:
        ind = 0
        linha += 1
        print(('B{}').format(linha),end='')
        for column in row:
            ind += 1
            if ind == 1:
                if linha == 10:
                    if column == 200:
                        print(('  {} ').format(0), end=" | ")
                    else:
                        print(('  {} ').format(column), end=" | ")
                else:
                    if column == 200:
                        print(('   {} ').format(0), end=" | ")
                    else:
                        print(('   {} ').format(column), end=" | ")
            elif ind == 10:
                if column == 200:
                    print((' {} ').format(0), end="")
                else:
                    print((' {} ').format(column), end="")

            else:
                if column == 200:
                    print((' {} ').format(0), end=" | ")
                else:
                    print((' {} ').format(column), end=" | ")
        print()
        print('    ',55*'-')

def imprimir_gameover(matriz):
    linha = 0
    print('     A1 -  A2 -  A3 -  A4 -  A5 -  A6 -  A7 -  A8 -  A9 -  A10')
    for row in matriz:
        ind = 0
        linha += 1
        print(('B{}').format(linha),end='')
        for column in row:
            ind += 1
            if ind == 1:
                if linha == 10:
                    print(('  {} ').format(column), end=" | ")
                else:
                    print(('   {} ').format(column), end=" | ")
            elif ind == 10:
                print((' {} ').format(column), end="")
            else:
                print((' {} ').format(column), end=" | ")
        print()
        print('    ',55*'-')
    print("\n     !!!!  BOOOMMMM   !!!!  ---  !!!!   VOCÊ EXPLODIU   !!!!")

def montar_bombas():
    for pos in range(10):
        pos_x = posicao_x[pos]
        pos_y = posicao_y[pos]
        tabuleiro[pos_y][pos_x] = 200

def montar_pos_x_y():
    ind = 0
    while ind < 10:
        num = randint(0,9)
        if num in posicao_x:
            continue
        else:
            posicao_x.append(num)
            ind += 1
    ind = 0
    while ind < 10:
        num = randint(0,9)
        if num in posicao_y:
            continue
        else:
            posicao_y.append(num)
            ind += 1

def verifica_posicao(x,y):
    x_new = x - 1
    y_new = y - 1
    if tabuleiro[x_new][y_new] == 200:
        tabuleiro[x_new][y_new] = '☠️'
        imprimir_gameover(tabuleiro)
        quit()
    else:
        tabuleiro[x_new][y_new] = '😜'

tabuleiro = []
posicao_x = []
posicao_y = []

pos_x = 0
pos_y = 0

montar_matriz()
montar_pos_x_y()
montar_bombas()

while True:
    imprimir_tabuleiro(tabuleiro)

    invalido = True
    while invalido:
        try:
            pos_A = int(input('Informe a posição A:'))
            if (pos_A < 1) or (pos_A > 10):
                print("Um numero entre 1 e 10!")
                invalido = True
            else:
                invalido = False
        except ValueError:
            print("Informe um numero valido!")
            continue

    invalido = True
    while invalido:
        try:
            pos_B = int(input('Informe a posição B:'))
            if (pos_B < 1) or (pos_B > 10):
                print("Um numero entre 1 e 10!")
                invalido = True
            else:
                invalido = False
        except ValueError:
            print("Informe um numero valido!")
            continue

    verifica_posicao(pos_B,pos_A)