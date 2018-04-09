# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Crie um programa que gere uma lista contendo 100 números aleatórios, e exiba esta lista na   ******
# ******             tela.                                                                                        ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import randint

lista_aleatorios = []

for _ in range(100):
    lista_aleatorios.append(randint(0,1000))

for l in lista_aleatorios:
    print('Elemento da lista: ', l)