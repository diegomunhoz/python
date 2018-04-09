# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Calcula o faroial de um numero informado pelo usuario               ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

def fatorial(num):
	if num<=1:
		return 1
	else:
		return num*fatorial(num-1)

num = int(input("Informe o numero e tecle <ENTER>:"))
print("Fatorial de", num, "é:", fatorial(num))
