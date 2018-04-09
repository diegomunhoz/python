# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa conversor de temperatura, que receba a temperatura ******
#                    em graus Celsius e converta-a para Fahrenheit e Kelvin              ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

celsius = int(input("Informe a temperatura:"))

fahrenheit = ((9/5) * celsius + 32)
kelvin = (celsius + 273.15)

print("Temperatura em Fahrenheit:", fahrenheit, "°")
print("Temperatura em Kelvin....:", kelvin, "°")
