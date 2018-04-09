# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa que que solicite ao usuário, para que digite 4     ******
# ******             notas e calcule a média artimética.                                 ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 03/04/2018                                                          ******
# *********************************************************************************************

nota1 = int(input("Informe a 1° Nota:"))
nota2 = int(input("Informe a 2° Nota:"))
nota3 = int(input("Informe a 3° Nota:"))
nota4 = int(input("Informe a 4° Nota:"))

print(
    "O valor da média é:",
    (nota1 +
     nota2 +
     nota3 +
     nota4)/4
)