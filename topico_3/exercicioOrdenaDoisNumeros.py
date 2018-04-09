# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um programa que solicite ao usuário para digitar 2 números,    ******
# ******             armazene-os nas variáveis a e b. Depois mostre estes 2 números em   ******
# ******             ordem crescente.                                                    ******
# ******             número é par ou ímpar.                                              ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

a = int(input("Informe o primeiro numero:"))
b = int(input("Informe o segundo numero.:"))

if a > b:
    print("Numero Ordenado:", b, "-", a)
else:
    print("Numero Ordenado:", a, "-", b)
