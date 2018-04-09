# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um programa que peça ao usuário para digitar 2 numeros inteiros e em seguida mostre-os  ******
# ******             em ordem crescente.                                                                          ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

lista_numeros = []

for num in range(1,3):
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

lista_numeros.sort()

print("\nLista em ordem crescente:", end=' ')

for l in lista_numeros:
    print(l, end=' ')