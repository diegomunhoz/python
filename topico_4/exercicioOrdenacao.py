# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Crie uma função que receba uma matriz com 10 números e coloque-a em ordem crescente.         ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

def ordenacao(lista):
    lista.sort()
    print("\nLista em ordem crescente:", end=' ')
    for l in lista:
        print(l, end=' ')

lista_numeros = []

for num in range(1,11):
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

ordenacao(lista_numeros)