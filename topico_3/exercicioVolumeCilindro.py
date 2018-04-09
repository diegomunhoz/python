# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que calcule o volume de um cilindro                ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 03/04/2018                                                          ******
# *********************************************************************************************

pi = 3.141592

raio = int(input("Informe a raio do circulo:"))
altura = int(input("Informe a raio do circulo:"))

area = (pi*(raio**2))
volume = area * altura

print("O volume do cilindro é:", volume)