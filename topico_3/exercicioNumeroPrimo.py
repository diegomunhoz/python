# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Crie um programa para informar se um número é primo ou não.         ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

numero = int(input("Digite um número: "))
aux = numero - 1

if (numero == 1):
    print("Você digitou o número 1")
else:
    while (True):
        if (aux == 1):
            print("É primo:", numero)
            break
        elif (numero % aux == 0):
            print("Não é primo:", numero)
            break
        elif (numero % aux != 0):
            aux -= 1
