# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Imprime um X                                                        ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

ini = 1
fim = 2
laco = 0
espaco = ' '
tamIntervalo = 16
tamInicio = 0

while laco != 2:
    for a in range(1, 9):

        if (tamIntervalo != 0):
            print(tamInicio*espaco, "*", tamIntervalo*espaco, "*")
        else:
            print('',tamInicio*espaco, "**")

        if laco == 0:
            tamIntervalo -= 2
            tamInicio += 1
        else:
            tamIntervalo += 2
            tamInicio -= 1

    tamIntervalo = 0
    tamInicio = 8
    laco += 1