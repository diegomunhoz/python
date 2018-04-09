# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: O jogo do estilingue consiste em jogar uma pedra do térreo para quebrar uma janela do        ******
# ******             edifício com 15 andares.                                                                     ******
# ******             No inicio do jogo o computador informará qual sua distância do prédio em metros e qual andar ******
# ******             que a janela deve ser acertada.                                                              ******
# ******             O objetivo do jogador consiste em informar o ângulo correto para arremessar a pedra.         ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 03/04/2018                                                                                   ******
# **********************************************************************************************************************

from random import randint
import math

alturaMaxima = 0
alturaMinima = 0

alturaAndar = 3

numeroAndar = 0
numeroAndar = randint(1,15)

distanciaPredio = 0
distanciaPredio = randint(5,100)

alturaMaxima = numeroAndar * alturaAndar
alturaMinima = (numeroAndar - 1) * alturaAndar

print("                   _________")
print("                  | O  O  O |")
print("                 /| O  O  O |")
print(("                / | O  O  O | (h) = {} metros").format(alturaMaxima))
print("               /  | O  O  O |  Altura")
print("              /   | O  O  O |                  ")
print("  Distância  /    | O  O  O |")
print("        (d) /     | O  O  O |")
print("    O      /      | O  O  O |")
print("   \|/    /       | O  O  O |")
print("    |    /        | O  O  O |  Número do andar que a ")
print(("   / \  /a)angulo | O  O  O |  janela deve ser acertada: {}° Andar").format(numeroAndar))
print("        -----------")
print("            (x)  ")
print(("          Distância do prédio: {}").format(distanciaPredio))

invalido = True
while invalido:
    try:
        angulo = int(input("Informe o angulo:"))
        if (angulo <= 0):
            print("Informe um valor maior que 0 <ZERO>:")
            invalido = True
        else:
            invalido = False
    except ValueError:
        print("Informe um valor maior que 0 <ZERO>!")
        continue

cosAngulo = math.cos(angulo)
cosAnguloConvertido = math.degrees(cosAngulo)

senAngulo = math.sin(angulo)
senAnguloConvertido = math.degrees(senAngulo)

valorX = int(distanciaPredio * cosAnguloConvertido)
valorY = int(distanciaPredio * senAnguloConvertido)

if valorX == distanciaPredio:
    if  (valorY >= alturaMinima) and (valorY <= alturaMaxima):
        print(("Você acertou a pedra no {}° andar").format(numeroAndar))
    else:
        print("Você errou a pedra!!")
else:
    print("Você errou a pedra!!")