# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Validação dos dados digitados pelo usuario                                                   ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

invalido = True

while invalido:
    try:
        input_numero = int(input("Informe o angulo:"))
        if (input_numero < 0):
            print("Informe um valor maior que 0 <ZERO>")
            invalido = True
        else:
            invalido = False
    except ValueError:
        print("Informe um numero valido!")
        continue

print("Valido!")
