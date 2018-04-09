# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que exiba um quadrado com 5 linha por 5 colunas e  ******
# ******             preenchimento vazio utilizando o caractere (177 -> 0xB1 ou 0xDB)    ******
# ******   Desafio : Modifique o programa e o tamanho do quadro para imprimir            ******
# ******             o texto “Linguagem de Programação C” dentro do quadro.              ******
# ******   Desafio II : Modifique o programa para imprimir tudo isso usando              ******
# ******             apenas uma linha de printf                                          ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 03/04/2018                                                          ******
# *********************************************************************************************

caracter = u'\u00b1'
vazio = ' '
texto = 'Linguagem de Programação C'

print('', (30*caracter),
      '\n',caracter,26*vazio,caracter,
      '\n',caracter,texto,caracter,
      '\n',caracter,26*vazio,caracter,
      '\n',(30*caracter)
)