# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um pequeno programa que solicite um número positivo ao usuário ******
# ******             e liste todos os números de 1 ao número informado, juntamente com a ******
# ******             soma.                                                               ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 04/04/2018                                                          ******
# *********************************************************************************************

soma = 0
numero = int(input("Informe um numero:"))

for n in range(1,(numero+1)):
    soma += n
    print(n)

print("\nTotal = {}".format(soma))