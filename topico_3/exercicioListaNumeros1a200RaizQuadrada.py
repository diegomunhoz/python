# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que liste do numero 1 ao 200 e também mostre a     ******
# ******             raiz quadrada do numero na mesma linha.                             ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 03/04/2018                                                          ******
# *********************************************************************************************

from math import sqrt

print('Numero - Raiz')
for numero in range(1,201):
    print('  ',numero, '  -  ', sqrt(numero))