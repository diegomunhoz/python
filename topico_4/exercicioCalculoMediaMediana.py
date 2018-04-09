# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Além da média aritmética existe a Mediana, que consiste no valor do meio de um conjunto de   ******
# ******             dados que tenha sido ordenado. A Mediana é utilizada na estatística para identificar os      ******
# ******             valores médios dos conjuntos de dados, e como se trata de um valor do meio do conjunto de    ******
# ******             dados, este valor não é facilmente afetado quando existem valores discrepantes no conjunto.  ******
# ******             Regra-1: quando o conjunto de dados possui uma quantidade impar de dados, então a mediana    ******
# ******                      será exatamente o valor localizado no meio do conjunto. Regra-2 quando o conjunto   ******
# ******                      de dados possui uma quantidade par de elementos, então a mediana será a media       ******
# ******                      aritmética dos dois elementos centrais                                              ******
# ******             Exemplo: Conjunto de dados = 7, 144, 32, 2, 9, 13, 20, 56, 50, 75, 8                         ******
# ******                      Conjunto de dados Ordenado = 2, 7, 8, 9, 13, 20, 32, 50, 56, 75, 144                ******
# ******                      Mediana = 20                                                                        ******
# ******             Exemplo2: (Quantidade de elementos pares)                                                    ******
# ******                      Conjunto de dados Ordenado = 2, 7, 8, 9, 13, 20, 32, 50, 56, 60, 75, 144            ******
# ******                      Mediana = ( 20 + 32 ) / 2 = 26                                                      ******
# ******             Faça um programa que peça ao usuário para entrar em 20 números, colocando estes números em   ******
# ******             um vetor, depois informe ao usuário a média aritmética deste conjunto de dados, juntamente   ******
# ******             com a mediana.                                                                               ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

import statistics

lista_numeros = []

for num in range(1,21):
    invalido = True
    while invalido:
        try:
            input_numero = int(input(("Informe o {}° numero:").format(num)))
            if (input_numero < 0):
                print("Informe um valor maior que 0 <ZERO>")
                invalido = True
            else:
                invalido = False
        except ValueError:
            print("Informe um numero valido!")
            continue

    lista_numeros.append(input_numero)

# Ordena a lista
lista_numeros.sort()

print("\nElementos da lista:", end=' ')

for l in lista_numeros:
    print(l, end=' ')

print(("\nMedia aritmética: {}").format(statistics.mean(lista_numeros)))
print(("Mediana da lista: {}").format(statistics.median(lista_numeros)))