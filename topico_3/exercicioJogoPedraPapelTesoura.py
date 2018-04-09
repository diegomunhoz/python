# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um jogo de pedra, papel e tesoura, faça com que o jogador      ******
# ******             informe se deseja jogar Pedra, Papel ou Tesoura, e faça com que     ******
# ******             o computador escolha aleatoriamente também Pedra, Papel ou Tesoura. ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 04/04/2018                                                          ******
# *********************************************************************************************

from random import choice

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

computador = ['Pedra','Papel','Tesoura']
opcaoComputador = choice(computador)

invalido = True
while invalido:
    try:
        numJogador = int(input("Informe a opção:"))
        if (numJogador != 1) and (numJogador != 2) and (numJogador != 3):
            print("Informe apenas as opções disponiveis!")
            invalido = True
        else:
            invalido = False
    except ValueError:
        print("Informe apenas as opções disponiveis!")
        continue

if  numJogador == 1:
    opcaoJogador = 'Pedra'
elif numJogador == 2:
    opcaoJogador = 'Papel'
else:
    opcaoJogador = 'Tesoura'

print('Opção do Jogador...: ', opcaoJogador)
print('Opção do Computador: ', opcaoComputador)

if opcaoComputador == opcaoJogador:
    print("Houve Empate!")
    quit()

if opcaoComputador == 'Pedra' and opcaoJogador == 'Tesoura':
    print("O computador ganhou!!")
elif opcaoComputador == 'Tesoura' and opcaoJogador == 'Papel':
    print("O computador ganhou!!")
elif opcaoComputador == 'Papel' and opcaoJogador == 'Pedra':
    print("O computador ganhou!!")
elif opcaoJogador == 'Pedra' and opcaoComputador == 'Tesoura':
    print("Você ganhou!!")
elif opcaoJogador == 'Tesoura' and opcaoComputador == 'Papel':
    print("Você ganhou!!")
else:
    print("Você ganhou!!")