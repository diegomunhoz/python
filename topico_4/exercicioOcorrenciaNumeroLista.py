# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Usando como base o programa do Exercício - Verificar se o número encontra-se na lista,       ******
# ******             adicione um código para informar quantas ocorrências deste número existem na lista.          ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import randint

repetido = 0
lista_aleatorios = []

for pos in range(100):
    lista_aleatorios.append(randint(0,100))

numero = int(input("Digite um numero:"))

for l in lista_aleatorios:
    if l == numero:
        repetido += 1

if repetido > 0:
    print(("O numero {} se repete {} vezes.").format(numero,repetido))
else:
    print("O numero não está na lista")