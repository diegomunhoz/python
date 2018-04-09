# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Mudar o jogo do Piratas do Caribe, para que o jogador ganhe quando
# ******             acertar a maior frequência de números dos dados, tornando o jogo
# ******             semelhante aquele conhecido como Jogo do Dado Mentiroso.            ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 04/04/2018                                                          ******
# *********************************************************************************************

from random import choice
from random import randint

def exibeDadosJogador():
    print(("*** Resultado dos {} dados do jogador ***").format(numeroDadosJogador))
    if numeroDadosJogador == 1:
        print("Dado 1:", opcaoDado1Jogador)
    elif numeroDadosJogador == 2:
        print("Dado 1:", opcaoDado1Jogador)
        print("Dado 2:", opcaoDado2Jogador)
    elif numeroDadosJogador == 3:
        print("Dado 1:", opcaoDado1Jogador)
        print("Dado 2:", opcaoDado2Jogador)
        print("Dado 3:", opcaoDado3Jogador)
    elif numeroDadosJogador == 4:
        print("Dado 1:", opcaoDado1Jogador)
        print("Dado 2:", opcaoDado2Jogador)
        print("Dado 3:", opcaoDado3Jogador)
        print("Dado 4:", opcaoDado4Jogador)
    else:
        print("Dado 1:", opcaoDado1Jogador)
        print("Dado 2:", opcaoDado2Jogador)
        print("Dado 3:", opcaoDado3Jogador)
        print("Dado 4:", opcaoDado4Jogador)
        print("Dado 5:", opcaoDado5Jogador)

def exibeDadosComputador():
    print(("*** Resultado dos {} dados do computador ***").format(numeroDadosComputador))
    if numeroDadosComputador == 1:
        print("Dado 1:", opcaoDado1Computador)
    elif numeroDadosComputador == 2:
        print("Dado 1:", opcaoDado1Computador)
        print("Dado 2:", opcaoDado2Computador)
    elif numeroDadosComputador == 3:
        print("Dado 1:", opcaoDado1Computador)
        print("Dado 2:", opcaoDado2Computador)
        print("Dado 3:", opcaoDado3Computador)
    elif numeroDadosComputador == 4:
        print("Dado 1:", opcaoDado1Computador)
        print("Dado 2:", opcaoDado2Computador)
        print("Dado 3:", opcaoDado3Computador)
        print("Dado 4:", opcaoDado4Computador)
    else:
        print("Dado 1:", opcaoDado1Computador)
        print("Dado 2:", opcaoDado2Computador)
        print("Dado 3:", opcaoDado3Computador)
        print("Dado 4:", opcaoDado4Computador)
        print("Dado 5:", opcaoDado5Computador)

numeroDadosJogador = int(input("Informe o numero de dados que ira jogar:"))
palpiteQtdeJogador = int(input("Palpite da quantidade de dados \nque o computador irá jogar:"))
palpiteNumJogador = int(input(("Palpite do numero sorteado nos {} \ndados do computador:").format(palpiteQtdeJogador)))

quantidadeComputador = [1,2,3,4,5]
numeroComputador = [1,2,3,4,5,6]

palpiteQtdeComputador = choice(quantidadeComputador)
palpiteNumComputador = choice(numeroComputador)

numeroDadosComputador = 0
numeroDadosComputador = randint(1,5)

resultadoJogador = []
resultadoComputador = []

dado1Jogador = [1,2,3,4,5,6]
dado2Jogador = [1,2,3,4,5,6]
dado3Jogador = [1,2,3,4,5,6]
dado4Jogador = [1,2,3,4,5,6]
dado5Jogador = [1,2,3,4,5,6]

dado1Computador = [1,2,3,4,5,6]
dado2Computador = [1,2,3,4,5,6]
dado3Computador = [1,2,3,4,5,6]
dado4Computador = [1,2,3,4,5,6]
dado5Computador = [1,2,3,4,5,6]

opcaoDado1Jogador = choice(dado1Jogador)
opcaoDado2Jogador = choice(dado2Jogador)
opcaoDado3Jogador = choice(dado3Jogador)
opcaoDado4Jogador = choice(dado4Jogador)
opcaoDado5Jogador = choice(dado5Jogador)

opcaoDado1Computador = choice(dado1Computador)
opcaoDado2Computador = choice(dado2Computador)
opcaoDado3Computador = choice(dado3Computador)
opcaoDado4Computador = choice(dado4Computador)
opcaoDado5Computador = choice(dado5Computador)

if (numeroDadosJogador == 1):
    resultadoJogador.append(opcaoDado1Jogador)
elif (numeroDadosJogador == 2):
    resultadoJogador.append(opcaoDado1Jogador)
    resultadoJogador.append(opcaoDado2Jogador)
elif (numeroDadosJogador == 3):
    resultadoJogador.append(opcaoDado1Jogador)
    resultadoJogador.append(opcaoDado2Jogador)
    resultadoJogador.append(opcaoDado3Jogador)
elif (numeroDadosJogador == 4):
    resultadoJogador.append(opcaoDado1Jogador)
    resultadoJogador.append(opcaoDado2Jogador)
    resultadoJogador.append(opcaoDado3Jogador)
    resultadoJogador.append(opcaoDado4Jogador)
else:
    resultadoJogador.append(opcaoDado1Jogador)
    resultadoJogador.append(opcaoDado2Jogador)
    resultadoJogador.append(opcaoDado3Jogador)
    resultadoJogador.append(opcaoDado4Jogador)
    resultadoJogador.append(opcaoDado5Jogador)

if (numeroDadosComputador == 1):
    resultadoComputador.append(opcaoDado1Computador)
elif (numeroDadosComputador == 2):
    resultadoComputador.append(opcaoDado1Computador)
    resultadoComputador.append(opcaoDado2Computador)
elif (numeroDadosComputador == 3):
    resultadoComputador.append(opcaoDado1Computador)
    resultadoComputador.append(opcaoDado2Computador)
    resultadoComputador.append(opcaoDado3Computador)
elif (numeroDadosComputador == 4):
    resultadoComputador.append(opcaoDado1Computador)
    resultadoComputador.append(opcaoDado2Computador)
    resultadoComputador.append(opcaoDado3Computador)
    resultadoComputador.append(opcaoDado4Computador)
else:
    resultadoComputador.append(opcaoDado1Computador)
    resultadoComputador.append(opcaoDado2Computador)
    resultadoComputador.append(opcaoDado3Computador)
    resultadoComputador.append(opcaoDado4Computador)
    resultadoComputador.append(opcaoDado5Computador)

erroJogador = 0
erroComputador= 0

acertoJogador = 0
acertoComputador = 0

for l in resultadoJogador:
    if (l == palpiteNumComputador):
        acertoComputador += 1
    else:
        erroComputador += 1

for l in resultadoComputador:
    if (l == palpiteNumJogador):
        acertoJogador += 1
    else:
        erroJogador += 1

if ((acertoJogador == palpiteQtdeJogador) and (acertoComputador == palpiteQtdeComputador)) and \
   ((erroComputador == 0) and (erroJogador == 0)):
    print("Houve empate entre jogador e o computador!!")
    print(("Palpite do jogador: {} dados de {}").format(palpiteQtdeJogador,palpiteNumJogador))
    print(("Palpite do computador: {} dados de {}").format(palpiteQtdeComputador,palpiteNumComputador))
elif (acertoJogador == palpiteQtdeJogador) and (erroJogador == 0):
    print("O jogador ganhou!!")
    print(("Palpite do jogador: {} dados de {}").format(palpiteQtdeJogador,palpiteNumJogador))
    print(("Palpite do computador: {} dados de {}").format(palpiteQtdeComputador,palpiteNumComputador))
elif (acertoComputador == palpiteQtdeComputador) and (erroComputador == 0):
    print("O computador ganhou!!")
    print(("Palpite do computador: {} dados de {}").format(palpiteQtdeComputador,palpiteNumComputador))
    print(("Palpite do jogador: {} dados de {}").format(palpiteQtdeJogador,palpiteNumJogador))
else:
    print("Ninguem acertou!")
    print(("Palpite do jogador: {} dados de {}").format(palpiteQtdeJogador,palpiteNumJogador))
    print(("Palpite do computador: {} dados de {}").format(palpiteQtdeComputador,palpiteNumComputador))

exibeDadosJogador()
exibeDadosComputador()