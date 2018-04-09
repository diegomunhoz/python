# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um jogo de dados, semelhante ao do Piratas do Caribe.          ******
# ******             O computador sorteará números para 6 dados, e somará todos estes    ******
# ******             valores.                                                            ******
# ******             Cabe ao jogador acertar qual é a soma de todos os seis dados        ******
# ******             O computador também tentará acertar a soma, para isto ele deve      ******
# ******             escolher um número aleatório entre 6 e 36.                          ******
# ******             Caso o jogador não acerte a soma, então deverá verificar se o número******
# ******             ficou mais próximo da soma do que o número escolhido pelo computador******
# ******             informe se deseja jogar Pedra, Papel ou Tesoura, e faça com que     ******
# ******             o computador escolha aleatoriamente também Pedra, Papel ou Tesoura. ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 04/04/2018                                                          ******
# *********************************************************************************************

from random import choice

def verificarPalpite(jogador, computador, resultado):
    diferencaJogador = 0
    diferencaComputador = 0

    if resultado > jogador:
        diferencaJogador = resultado - jogador
    else:
        diferencaJogador = jogador - resultado

    if resultado > computador:
        diferencaComputador = resultado - computador
    else:
        diferencaComputador = computador - resultado

    if diferencaJogador == diferencaComputador:
        print("Houve empate!")
    elif diferencaComputador < diferencaJogador:
        print('O computador venceu, palpite mais proximo!')
    else:
        print('O jogador venceu, palpite mais proximo!')

computador = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
palpiteCOmputador = choice(computador)

dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]
dado3 = [1,2,3,4,5,6]
dado4 = [1,2,3,4,5,6]
dado5 = [1,2,3,4,5,6]
dado6 = [1,2,3,4,5,6]

opcaoDado1 = choice(dado1)
opcaoDado2 = choice(dado2)
opcaoDado3 = choice(dado3)
opcaoDado4 = choice(dado4)
opcaoDado5 = choice(dado5)
opcaoDado6 = choice(dado6)

resultadoSoma = (opcaoDado1 + opcaoDado2 + opcaoDado3 + opcaoDado4 + opcaoDado5 + opcaoDado6)

invalido = True
while invalido:
    try:
        palpiteJogador = int(input("Informe um valor entre 6 e 36:"))
        if (palpiteJogador < 6) or (palpiteJogador > 36):
            print("Um numero entre 6 e 36!")
            invalido = True
        else:
            invalido = False
    except ValueError:
        print("Um numero entre 6 e 36!")
        continue

print('Dado 1:',opcaoDado1)
print('Dado 2:',opcaoDado2)
print('Dado 3:',opcaoDado3)
print('Dado 4:',opcaoDado4)
print('Dado 5:',opcaoDado5)
print('Dado 6:',opcaoDado6)
print('Resultado da soma dos dados:',resultadoSoma)

print('Palpite do Jogador.........:', palpiteJogador)
print('Palpite do Computador......:', palpiteCOmputador)

if (palpiteJogador == resultadoSoma) and (palpiteCOmputador == resultadoSoma):
    print('Houve empate, jogador e computador acertaram o palpite!')
elif palpiteJogador == resultadoSoma:
    print('O jogador venceu, acertou o palpite!')
elif palpiteCOmputador == resultadoSoma:
    print('O computador venceu, acertou o palpite!')
else:
    verificarPalpite(palpiteJogador, palpiteCOmputador, resultadoSoma)