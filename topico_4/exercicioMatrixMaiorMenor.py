# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Faça um programa que peça ao usuário para digitar 5 numeros inteiros e em seguida:           ******
# ******             a) mostre os 5 numeros na tela.                                                              ******
# ******             b) mostre qual dos 5 números é o maior.                                                      *****(
# ******             c) mostra qual dos 5 números é o menor.                                                      ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

lista_numeros = []


for n in range(1,6):
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

print("\nElementos da lista:", end=' ')

for l in lista_numeros:
    print(l, end=' ')

lista_numeros.sort()

print(("\nMaior elemento: {}").format(lista_numeros[(len(lista_numeros)-1)]))
print(("Menor elemento: {}").format(lista_numeros[0]))