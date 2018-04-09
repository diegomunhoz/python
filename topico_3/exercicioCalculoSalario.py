# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa para auxiliar a calcular o salário no final do mês ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

horas = int(input("Horas trabalhadas no mês:"))
valor_hora = int(input("Valor da hora trabalhada:"))
percentual = int(input("Percentual de desconto:"))

salario_bruto = (horas * valor_hora)
percentual_desconto = (percentual * salario_bruto)/100
salario_liquido = salario_bruto - percentual_desconto

print("Salario Bruto.........: R$", salario_bruto)
print("Total a ser descontado: R$", percentual_desconto)
print("Salário Liquido.......: R$", salario_liquido)