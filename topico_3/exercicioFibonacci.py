# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um programa que imprima a sequencia de Fibonacci               ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

fimFibonacci = int(input("Informe um numero:"))

vlA, vlB = 0, 1
print(vlA)
while (vlB < fimFibonacci):
    vlA, vlB = vlB, vlA + vlB
    print(vlA)

