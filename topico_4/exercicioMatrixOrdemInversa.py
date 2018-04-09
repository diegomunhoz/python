# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um programa que solicite ao usuário para digitar 20 números, guarde-os em um vetor do   ******
# ******             tipo inteiro e depois exiba-os na tela na ordem inversa em foram inseridos.                  ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

lista_numeros = []

for n in range(1,21):
    lista_numeros.append(int(input(("Informe o {}° numero:").format(n))))

# Inverte a lista
lista_numeros.reverse()

print("Elementos da Lista: ", end='')
for l in lista_numeros:
    print(l, end=' ')