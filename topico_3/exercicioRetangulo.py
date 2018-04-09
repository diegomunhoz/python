# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Programa para imprimir um retangulo com altura e comprimento        ******
# ******             informados pelo usuario                                             ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

ini = 0

comprimento = int(input("Informe o comprimento do retangulo:"))
altura = int(input("Informe a altura do retangulo:"))

for alt in range(ini,altura):
    for cmp in range(ini,comprimento):
        print(
            "x", end=''
        )
    print("")