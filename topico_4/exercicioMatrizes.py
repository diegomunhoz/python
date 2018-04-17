# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: 1) Faça um programa que solicite informações do usuario para construir duas matrizes com o   ******
# ******                tamanho [2x2].                                                                            ******
# ******             2) Modifique o programa anterior para oferecer as seguintes opções para o usuario :          ******
# ******                a) Adição das matrizes                                                                    ******
# ******                b) Multiplicação da Matriz 1 pela Matriz 2                                                ******
# ******                c) Multiplicação da Matriz 2 pela Matriz 1                                                ******
# ******                d) Subtração da Matriz 1 pela Matriz 2                                                    ******
# ******                e) Subtração da Matriz 2 pela Matriz 1                                                    ******
# ******                f) Matriz Identidade                                                                      ******
# ******                g) Matriz Inversa                                                                         ******
# ******             Faça uma função para retornar cada uma destas soluções. As funções deverão receber matrizes  ******
# ******             como parâmetro e retornar uma matriz de resposta.                                            ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

import random
import numpy as np
from numpy import linalg

def imprimir_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        print('[', end='')
        for j in range(colunas):
            if(j == colunas - 1):
                print("%s" %matriz[i][j],end='')
            else:
                print("%s" %matriz[i][j], end = " ")
        print(']')
    print()

def somar_matriz(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

def multiplicar_matriz(m1,m2):
    result = [[0, 0],
              [0, 0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def subtrair_matriz(m1,m2):
    result = []
    result = np.absolute(np.array(m1) - np.array(m2))
    return result

def matriz_inversa(m1):
    result = []
    result = linalg.inv(m1)
    return result

def matriz_identidade(tam):
    result = [[0 for x in range(tam)] for y in range(tam)]
    for i in range(0,tam):
        result[i][i] = 1
    return result

matriz1 = []
matriz2 = []

print("Informe os valores da 1ª Matriz:")
for i in range(2):
     matriz1.append([])
     for j in range(2):

        invalido = True
        while invalido:
            try:
                numero = int(input(("Elemento da {}° linha e {}° coluna:").format(i+1,j+1)))
                if (numero < 0):
                    print("Um numero maior que 0 <ZERO>!")
                    invalido = True
                else:
                    invalido = False
            except ValueError:
                print("Informe um numero valido!")
                continue

        matriz1[i].append(numero)

print("Informe os valores da 2ª Matriz:")
for i in range(2):
     matriz2.append([])
     for j in range(2):

        invalido = True
        while invalido:
            try:
                numero = int(input(("Elemento da {}° linha e {}° coluna:").format(i+1,j+1)))
                if (numero < 0):
                    print("Um numero maior que 0 <ZERO>!")
                    invalido = True
                else:
                    invalido = False
            except ValueError:
                print("Informe um numero valido!")
                continue
        matriz2[i].append(numero)

print("\nOperações com Matrizes:\n")

print("Matriz 1:")
imprimir_matriz(matriz1)

print("Matriz 2:")
imprimir_matriz(matriz2)

print("Adição das matrizes:")
imprimir_matriz(somar_matriz(matriz1, matriz2))


print("Multiplicação da Matriz 1 pela Matriz 2:")
imprimir_matriz(multiplicar_matriz(matriz1,matriz2))

print("Multiplicação da Matriz 2 pela Matriz 1:")
imprimir_matriz(multiplicar_matriz(matriz2,matriz1))

print("Subtração da Matriz 1 pela Matriz 2:")
imprimir_matriz(subtrair_matriz(matriz1,matriz2))

print("Subtração da Matriz 2 pela Matriz 1:")
imprimir_matriz(subtrair_matriz(matriz2,matriz1))

print("Matriz Identidade:")
imprimir_matriz(matriz_identidade(2))

print("Matriz Inversa:")
imprimir_matriz(matriz_inversa(matriz1))