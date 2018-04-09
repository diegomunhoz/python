# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Imprime uma piramide na tela                                        ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

laco = 0
tam = 1

comprimento = int(input("Informe o tamanho da pirâmide:"))
comprimento += 1

while laco != 2:

    for a in range(1, comprimento):
        print(tam * '*')

        if laco == 0:
            tam += 1
        else:
            tam -= 1

    tam = comprimento - 1
    laco += 1