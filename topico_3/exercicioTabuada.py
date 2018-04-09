# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Tabuada de um numero especifico informado pelo usuario              ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

multiplicando = int(input("TABUADA DO:"))

for multiplicador in range(1,11):
    print(multiplicando, "x", multiplicador, ":", (multiplicando * multiplicador))