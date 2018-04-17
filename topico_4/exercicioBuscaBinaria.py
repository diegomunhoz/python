# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um função que efetue uma busca binária em um vetor ordenado. Para isto a função deverá
# ******             receber como parâmetro um vetor de números inteiros, e como segundo parâmetro um número
# ******             inteiro o qual deverá ser pesquisado no vetor.
# ******             Se o número passado como parâmetro for encontrado no vetor, a função deverá retornar o       ******
# ******             índice de sua posição no vetor, caso contrário ela deverá retornar -1                        ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

import random

# Método de buscar binária interativa
def buscaIterativa(vetor, numero):
	esquerda, direita, tentativa = 0, len(vetor), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_num = vetor[meio]
		if numero == aux_num:
			return tentativa
		elif numero > aux_num:
			esquerda = meio
		else:
			direita = meio
		tentativa += 1

# Método de buscar binária recursiva
def buscaRecursiva(vetor, numero, esquerda, direita, tentativa):
	meio = (esquerda + direita) // 2
	aux_num = vetor[meio]
	if numero == aux_num:
		return tentativa
	elif numero > aux_num:
		return buscaRecursiva(vetor, numero, meio, direita, tentativa + 1)
	return buscaRecursiva(vetor, numero, esquerda, meio, tentativa + 1)

vetor = [i for i in range(1, 1000001)]
numero = random.choice(vetor)
print('Numero escolhido: %d' % numero)
print('Tentativa (iterativo): %d' % buscaIterativa(vetor, numero))
print('Tentativa (recursivo): %d' % buscaRecursiva(vetor, numero, 0, len(vetor), 1))