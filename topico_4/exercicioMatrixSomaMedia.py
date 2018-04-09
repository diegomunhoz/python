# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um programa que solicite ao usuário para digitar 20 números, guarde-os em um vetor do   ******
# ******             tipo inteiro e depois exiba-os na tela. Para cada número exibido, mostre também a soma e a   ******
# ******             média aritmética até o momento.                                                              ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

lista_numeros = []
soma = 0
media = 0
qtd_lista = 0

for n in range(1,21):
    lista_numeros.append(int(input(("Informe o {}° numero:").format(n))))

print("\nNumero   Soma   Media")

for l in lista_numeros:
    qtd_lista += 1
    soma += l
    media = (soma / qtd_lista)
    print(' ',l, '    ',soma, '    ',media)