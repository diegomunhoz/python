# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um programa que solicite ao usuário para digitar 3 números,    ******
# ******             armazene-os nas variáveis a, b e c                                  ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

a = int(input("Informe o 1° numero:"))
b = int(input("Informe o 2° numero:"))
c = int(input("Informe o 3° numero:"))

if a < b < c:
    print("Numeros ordenados:", a, "-", b, "-", c)
elif (a < c < b):
    print("Numeros ordenados:", a, "-", c, "-", b)
elif (b < a < c):
    print("Numeros ordenados:", b, "-", a, "-", c)
elif (b < c < a):
    print("Numeros ordenados:", b, "-", c, "-", a)
elif (c < a < b):
    print("Numeros ordenados:", c, "-", a, "-", b)
elif (c < b < a):
    print("Numeros ordenados:", c, "-", b, "-", a)
else:
    print("Não pode informar numeros iguais")