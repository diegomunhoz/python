# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que peça um número ao usuário e informe se este    ******
# ******             número é par ou ímpar.                                              ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

numero = int(input("Informe um numero:"))

if (numero % 2) == 0:
    print("Numero Par!")
else:
    print("Numero Impar!")