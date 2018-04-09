# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Neste exercício deverá ser feito um jogo de forca, o qual consiste em escolher uma palavra   ******
# ******             aleatória, e depois repetirá, pedindo ao jogador uma letra. Se a palavra aleatória contiver  ******
# ******             a letra então esta letra deverá ser mostrada na posição em que realmente se encontra.        ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import choice

ind = 0

lista_acertos = []

lista_palavras = ['FATEC','ELEICAO','DIRETORIA','ALUNO','PIRAMIDE','EXERCICIO','PYTHON']
palavra = choice(lista_palavras)

lista_letras = ['-' for _ in palavra]

lista_tentativas = []

jogando = True
while jogando:
    print('Adivinhe a palavra: ', lista_letras)

    invalido = True
    while invalido:
        try:
            letra_escolhida = str(input("Digite uma letra:")).upper()[0]

            if letra_escolhida in lista_tentativas:
                print("Você já usou esta letra, por favor digite outra:")
                invalido = True
            else:
                invalido = False
        except ValueError:
            print("Houve um erro!")
            continue

    lista_tentativas.append(letra_escolhida)
    print('Tentivas utilizadas:',lista_tentativas)
    for pos in range(len(palavra)):
        if (palavra[pos] == letra_escolhida):
            lista_letras[pos] = letra_escolhida

    if len(lista_tentativas) == 5:
        print("Você perdeu, usou todas as suas tentativas!")
        jogando = False
    else:
        if '-' in lista_letras:
            continue
        else:
            print('Você venceu!!')
            jogando = False