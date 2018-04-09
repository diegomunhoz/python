# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Imprime uma arvore de natal                                         ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

ini = 1
fim = 2
laco = 0
espaco = ' '
tam = 4

while laco != 5:
    print(tam*espaco,
          "/",
          end='')

    for a in range(1,fim):
        print("*", end='')

    tam -= 1
    fim += 2
    laco += 1

    print(u'\u005C')
else:
    laco = 0
    tam = 5

while laco != 3:
    print(tam * espaco, "||")
    laco += 1