# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Usando como base o programa do Exercício - Lista de números aleatórios, adicione um código   ******
# ******             para pedir ao usuário que digite um número, e depois mostre se este número encontra-se ou    ******
# ******             não na lista de números aleatórios.                                                          ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import randint

lista_aleatorios = []

for _ in range(100):
    lista_aleatorios.append(randint(0,100))

numero = int(input("Digite um numero:"))

if numero in lista_aleatorios:
    print("O numero encontra-se na lista")
else:
    print("O numero não encontra-se na lista")