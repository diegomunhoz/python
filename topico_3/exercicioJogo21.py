# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Neste exercício deverá ser feito um jogo de 21, este é um jogo de cartas que consiste em     ******
# ******             fornecer cartas para o jogador e para a banca. Inicialmente serão fornecidas 2 cartas para   ******
# ******             cada, e depois ambos tanto o jogador quanto a banca têm a opção de comprar mais cartas,      ******
# ******             sendo uma de cada vez.                                                                       ******
# ******   Regras..:
# ******             - O objetivo do jogo é fazer 21 exatos ou o maior número possível sem ultrapassar 21;        ******
# ******             - No término da rodada aquele que fizer 21 pontos exatos vence, e se ambos fizerem 21 pontos ******
# ******               a vitória pertencerá ao jogador;                                                           ******
# ******             - Se houver empate de pontos menores que 21, então a banca ganha;                            ******
# ******             - Em qualquer outra situação, que fizer mais pontos vence;                                   ******
# ******             - A carta “A” de qualquer naipe pode ter o valor 1 ou o valor 11, conforme a situação,       ******
# ******               aquilo que for mais benéfico para o jogador (Esta regra não precisa ser implementada       ******
# ******               neste momento)                                                                             ******
# ******   Desafio : Implemente a regra do “A”.                                                                   ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 03/04/2018                                                                                   ******
# **********************************************************************************************************************

import os
from random import choice

listaCartas = []

um_ouro = {"valor":1, "naipe":'♦️',"texto":'1 de Ouro'}
listaCartas.append(um_ouro)
um_espada = {"valor":1, "naipe":'♠️',"texto":'1 de Espada'}
listaCartas.append(um_espada)
um_copas = {"valor":1, "naipe":'♥️',"texto":'1 de Copas'}
listaCartas.append(um_copas)
um_paus = {"valor":1, "naipe":'♣️',"texto":'1 de Paus'}
listaCartas.append(um_paus)

dois_ouro = {"valor":2, "naipe":'♦️',"texto":'2 de Ouro'}
listaCartas.append(dois_ouro)
dois_espada = {"valor":2, "naipe":'♠️',"texto":'2 de Espada'}
listaCartas.append(dois_espada)
dois_copas = {"valor":2, "naipe":'♥️',"texto":'2 de Copas'}
listaCartas.append(dois_copas)
dois_paus = {"valor":2, "naipe":'♣️',"texto":'2 de Paus'}
listaCartas.append(dois_paus)

tres_ouro = {"valor":3, "naipe":'♦️',"texto":'3 de Ouro'}
listaCartas.append(tres_ouro)
tres_espada = {"valor":3, "naipe":'♠️',"texto":'3 de Espada'}
listaCartas.append(tres_espada)
tres_copas = {"valor":3, "naipe":'♥️',"texto":'3 de Copas'}
listaCartas.append(tres_copas)
tres_paus = {"valor":3, "naipe":'♣️',"texto":'3 de Paus'}
listaCartas.append(tres_paus)

quatro_ouro = {"valor":4, "naipe":'♦️',"texto":'4 de Ouro'}
listaCartas.append(quatro_ouro)
quatro_espada = {"valor":4, "naipe":'♠️',"texto":'4 de Espada'}
listaCartas.append(quatro_espada)
quatro_copas = {"valor":4, "naipe":'♥️',"texto":'4 de Copas'}
listaCartas.append(quatro_copas)
quatro_paus = {"valor":4, "naipe":'♣️',"texto":'4 de Paus'}
listaCartas.append(quatro_paus)

cinco_ouro = {"valor":5, "naipe":'♦️',"texto":'5 de Ouro'}
listaCartas.append(cinco_ouro)
cinco_espada = {"valor":5, "naipe":'♠️',"texto":'5 de Espada'}
listaCartas.append(cinco_espada)
cinco_copas = {"valor":5, "naipe":'♥️',"texto":'5 de Copas'}
listaCartas.append(cinco_copas)
cinco_paus = {"valor":5, "naipe":'♣️',"texto":'5 de Paus'}
listaCartas.append(cinco_paus)

seis_ouro = {"valor":6, "naipe":'♦️',"texto":'6 de Ouro'}
listaCartas.append(seis_ouro)
seis_espada = {"valor":6, "naipe":'♠️',"texto":'6 de Espada'}
listaCartas.append(seis_espada)
seis_copas = {"valor":6, "naipe":'♥️',"texto":'6 de Copas'}
listaCartas.append(seis_copas)
seis_paus = {"valor":6, "naipe":'♣️',"texto":'6 de Paus'}
listaCartas.append(seis_paus)

sete_ouro = {"valor":7, "naipe":'♦️',"texto":'7 de Ouro'}
listaCartas.append(sete_ouro)
sete_espada = {"valor":7, "naipe":'♠️',"texto":'7 de Espada'}
listaCartas.append(sete_espada)
sete_copas = {"valor":7, "naipe":'♥️',"texto":'7 de Copas'}
listaCartas.append(sete_copas)
sete_paus = {"valor":7, "naipe":'♣️',"texto":'7 de Paus'}
listaCartas.append(sete_paus)

oito_ouro = {"valor":8, "naipe":'♦️',"texto":'8 de Ouro'}
listaCartas.append(oito_ouro)
oito_espada = {"valor":8, "naipe":'♠️',"texto":'8 de Espada'}
listaCartas.append(oito_espada)
oito_copas = {"valor":8, "naipe":'♥️',"texto":'8 de Copas'}
listaCartas.append(oito_copas)
oito_paus = {"valor":8, "naipe":'♣️',"texto":'8 de Paus'}
listaCartas.append(oito_paus)

nove_ouro = {"valor":9, "naipe":'♦️',"texto":'9 de Ouro'}
listaCartas.append(nove_ouro)
nove_espada = {"valor":9, "naipe":'♠️',"texto":'9 de Espada'}
listaCartas.append(nove_espada)
nove_copas = {"valor":9, "naipe":'♥️',"texto":'9 de Copas'}
listaCartas.append(nove_copas)
nove_paus = {"valor":9, "naipe":'♣️',"texto":'9 de Paus'}
listaCartas.append(nove_paus)

dez_ouro = {"valor":10, "naipe":'♦️',"texto":'10 de Ouro'}
listaCartas.append(dez_ouro)
dez_espada = {"valor":10, "naipe":'♠️',"texto":'10 de Espada'}
listaCartas.append(dez_espada)
dez_copas = {"valor":10, "naipe":'♥️',"texto":'10 de Copas'}
listaCartas.append(dez_copas)
dez_paus = {"valor":10, "naipe":'♣️',"texto":'10 de Paus'}
listaCartas.append(dez_paus)

onze_ouro = {"valor":11, "naipe":'♦️',"texto":'11 de Ouro'}
listaCartas.append(onze_ouro)
onze_espada = {"valor":11, "naipe":'♠️',"texto":'11 de Espada'}
listaCartas.append(onze_espada)
onze_copas = {"valor":11, "naipe":'♥️',"texto":'11 de Copas'}
listaCartas.append(onze_copas)
onze_paus = {"valor":11, "naipe":'♣️',"texto":'11 de Paus'}
listaCartas.append(onze_paus)

def sorteiaCarta():
    carta = choice(listaCartas)
    listaCartas.remove(carta)
    return carta

def imprimeSorteio(valorJogador, naipeJogador,
                   valorComputador, naipeComputador,
                   totalJogador, totalComputador,
                   cartaSorteadaJogador, cartaSorteadaComputador):
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('CLS')

    caracter = u'\u00b1'
    print('Carta Jogador === Carta Computador')
    print(' {}          {}'.format(cartaSorteadaJogador,cartaSorteadaComputador))
    print(13*caracter,'   ',13*caracter)
    print('{} {}{}      '.format(caracter,valorJogador,naipeJogador),caracter,
          '   ',
          '{} {}{}       '.format(caracter, valorComputador, naipeComputador), caracter,
    )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
    )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
          )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)

          )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)

          )
    print('{}       {}{}'.format(caracter, naipeJogador, valorJogador), caracter,
          '   ',
          '{}        {}{}'.format(caracter, naipeComputador, valorComputador), caracter


          )
    print(13*caracter,'   ',13*caracter)
    print('    Total: {}'.format(totalJogador),
          '       ',
          'Total: {}'.format(totalComputador)
    )

def imprimeInicio(valor1Jogador, naipe1Jogador, valor2Jogador, naipe2Jogador,
                   valor1Computador, naipe1Computador,valor2Computador, naipe2Computador,
                   totalJogador, totalComputador):
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('CLS')

    caracter = u'\u00b1'
    print('        Cartas Jogador           ===            Cartas Computador')
    print(13*caracter,'   ',13*caracter, '         ',13*caracter,'   ',13*caracter)
    print('{} {}{}      '.format(caracter,valor1Jogador,naipe1Jogador),caracter,
          '   ',
          '{} {}{}       '.format(caracter, valor2Jogador, naipe2Jogador), caracter,

          '          {} {}{}      '.format(caracter, valor1Computador, naipe1Computador), caracter,
          '   ',
          '{} {}{}       '.format(caracter, valor2Computador, naipe2Computador), caracter,

    )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter),
          '         ',
          '{}           {}'.format(caracter, caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
    )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter),
          '         ',
          '{}           {}'.format(caracter, caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
          )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter),
          '         ',
          '{}           {}'.format(caracter, caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
          )
    print('{}           {}'.format(caracter,caracter),
          '   ',
          '{}           {}'.format(caracter, caracter),
          '         ',
          '{}           {}'.format(caracter, caracter),
          '   ',
          '{}           {}'.format(caracter, caracter)
          )
    print('{}       {}{}'.format(caracter, naipe1Jogador, valor1Jogador), caracter,
          '   ',
          '{}        {}{}'.format(caracter, naipe2Jogador, valor2Jogador), caracter,
          '         ',
          '{}       {}{}'.format(caracter, naipe1Computador, valor1Computador), caracter,
          '   ',
          '{}        {}{}'.format(caracter, naipe2Computador, valor2Computador), caracter)
    print(13*caracter,'   ',13*caracter,'         ',13*caracter,'   ',13*caracter)


    print('        Total Jogador: {}'.format(totalJogador),
          '                        Total Computador: {}'.format(totalComputador)
    )

vlAux = 0
jogando = True
opcao = ''
pontosJogador = 0
pontosComputador= 0

carta1Jogador = sorteiaCarta()
valorCarta1Jogador = carta1Jogador.get('valor')
naipeCarta1Jogador = carta1Jogador.get('naipe')
pontosJogador += valorCarta1Jogador

carta2Jogador = sorteiaCarta()
valorCarta2Jogador = carta2Jogador.get('valor')
naipeCarta2Jogador = carta2Jogador.get('naipe')
pontosJogador += valorCarta2Jogador

carta1Computador = sorteiaCarta()
valorCarta1Computador = carta1Computador.get('valor')
naipeCarta1Computador = carta1Computador.get('naipe')
pontosComputador += valorCarta1Computador

carta2Computador = sorteiaCarta()
valor2CartaComputador = carta2Computador.get('valor')
naipe2CartaComputador = carta2Computador.get('naipe')
pontosComputador += valor2CartaComputador

imprimeInicio(valorCarta1Jogador, naipeCarta1Jogador, valorCarta2Jogador, naipeCarta2Jogador,
              valorCarta1Computador, naipeCarta1Computador, valor2CartaComputador, naipe2CartaComputador,
              pontosJogador, pontosComputador)

opcao = input('Pressione <ENTER> para continuar o jogo e Boa Sorte!!')

while jogando:

    cartaJogador = sorteiaCarta()
    valorCartaJogador = cartaJogador.get('valor')
    naipeCartaJogador = cartaJogador.get('naipe')
    textoCartaJogador = cartaJogador.get('texto')

    cartaComputador = sorteiaCarta()
    valorCartaComputador = cartaComputador.get('valor')
    naipeCartaComputador = cartaComputador.get('naipe')
    textoCartaComputador = cartaComputador.get('texto')

    pontosJogador += valorCartaJogador
    pontosComputador += valorCartaComputador

    imprimeSorteio(valorCartaJogador,naipeCartaJogador,
             valorCartaComputador,naipeCartaComputador,
             pontosJogador,pontosComputador,
             textoCartaJogador, textoCartaComputador
    )

    if (pontosComputador == 21) and (pontosJogador == 21) :
        print("Vocês empataram!")
        break
    elif (pontosComputador > 21) and (pontosJogador < 21) :
        print("Você ganhou!")
        break
    elif (pontosComputador == 21) and (pontosJogador < 21) :
        print("Você perdeu marreco!")
        break

    if (pontosJogador <= 10):
        opcao = input("Sem dúvida, compre mais uma carta, pressione <ENTER> para continaur")
    elif (pontosJogador > 10) and (pontosJogador <= 15):
        opcao = input("Há um risco, mas aconselho a comprar mais uma carta, pressione <ENTER> para comprar")
    elif (pontosJogador > 15) and (pontosJogador <= 20):
        opcao = input("Aconselho a parar de jogar, pressione <ENTER> para comprar ou <N> para parar")
    elif (pontosJogador == 21):
        print("Você ganhou, não compre mais nada")
        jogando = False
        break
    else:
        print("Você perdeu")
        jogando = False
        break

    if (opcao == 'N') or (opcao == 'n'):
        if pontosComputador < pontosJogador:
            print("Você ganhou!")
            quit()
        elif pontosComputador > pontosJogador:
            print("Você perdeu!")
            quit()
        elif pontosComputador == pontosJogador:
            print("Você ganhou!")
            quit()
        else:
            print("Você ganhou!")
            quit()
    else:
        jogando = True