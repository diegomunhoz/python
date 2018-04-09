# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um programa que solicite ao usuário para digitar 20 números, guarde-os em um vetor do   ******
# ******             tipo inteiro e depois exiba-os na tela na ordem inversa em foram inseridos. Exiba também a   ******
# ******             soma de todos os números e a média aritmética.                                               ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

lista_numeros = []
soma = 0
media = 0
qtd_lista = 0

for n in range(1,21):
    invalido = True
    while invalido:
        try:
            input_numero = int(input(("Informe o {}° numero:").format(n)))
            if (input_numero < 0):
                print("Informe um valor maior que 0 <ZERO>")
                invalido = True
            else:
                invalido = False
        except ValueError:
            print("Informe um numero valido!")
            continue

    lista_numeros.append(input_numero)

# Inverte a lista
lista_numeros.reverse()

print("\nNumero   Soma   Media")
for l in lista_numeros:
    qtd_lista += 1
    soma += l
    media = (soma / qtd_lista)
    print(' ',l, '    ',soma, '    ',media)