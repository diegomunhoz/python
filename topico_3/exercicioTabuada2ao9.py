# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Tabuada do 02 ao 09                                                 ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

ini = 2
fim = 6
laco = 0

while (laco != 2):
    for multiplicador in range(1,11):
        for multiplicando in range(ini,fim):
            print(
                multiplicando, "x", multiplicador, "=", (multiplicando * multiplicador), end='      '
            )
        print("")
    ini = 6
    fim = 10
    laco += 1
    print(" ")
    print(" ")