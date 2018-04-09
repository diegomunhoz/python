# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que solicite ao usuário para digitar um número e   ******
# ******             exiba todos os números desde o informado pelo usuário até o número 1******
# ******             de maneira decrescente.                                             ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 03/04/2018                                                          ******
# *********************************************************************************************

numero = int(input("Informe um numero:"))
for numero in range(numero,0,-1):
    print(numero)