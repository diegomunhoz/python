# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um pequeno programa p/ simular um conselheiro para o jogo de 21******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************


apostaNumero = int(input("Digite o numero da aposta:"))

if (apostaNumero <= 10):
    print("Sem dúvida, compre mais uma carta")
elif(apostaNumero > 10) and (apostaNumero <= 15):
    print("Há um risco, mas aconselho a comprar mais uma carta")
elif(apostaNumero > 15) and (apostaNumero <= 20):
    print("Aconselho a parar de jogar")
elif(apostaNumero == 21):
    print("Você ganhou, não compre mais nada")
else:
    print("Você perdeu")