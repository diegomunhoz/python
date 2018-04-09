# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que liste todos os números de 2 a 30, juntamente   ******
# ******             com o fatorial do número.                                           ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

def fatorial(num):
	if num<=1:
		return 1
	else:
		return num*fatorial(num-1)

print('Numero - Fatorial')
for numero in range(2,31):
    print(numero,'  -  {}! ='.format(numero),fatorial(numero))

