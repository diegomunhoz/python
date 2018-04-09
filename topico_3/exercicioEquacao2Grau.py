# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Faça um programa chamado soma, o qual imprimirá o cabeçalho e       ******
# ******             solicitará ao usuário que digite dois números, após isso o programa ******
# ******             deve imprimir a soma dos números na tela.                           ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 17/03/2018                                                          ******
# *********************************************************************************************

#FUNÇÕES
def delta(a,b,c):
    delta = (b**2) - (4*a*c)
    return {"delta":delta}

def raizes(a,b,c,delta):
    x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
    x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
    return {"x1":x1,"x2":x2}

#PERGUNTA
def pergunta(valor):
    try:
        n = int(input("Qual o valor de %s:"%valor))
        return n
    except ValueError:
        n = " "
        return n

#PROGRAMA
valores = ["B","C"]
resposta = []
perguntarNovamente = None
numeroInvalido = True
laco = 0

while laco != 1:
    print("Equação de segundo grau - Solução \n(Delta,Raízes)")
    print()
    while numeroInvalido:
        try:
            a = int(input("Qual o valor de A: "))
            if a == 0:
                numeroInvalido = True
            else:
                numeroInvalido = False
        except ValueError:
            print("'A' Tem que ser um número!")
            continue

    numeroInvalido = True

    for valor in valores:
        perguntarNovamente = True
        while perguntarNovamente:
            res = pergunta(valor)
            if not(isinstance(res, int) or isinstance(res, float)):
                print()
                print("Valor inválido!")
                continue
            else:
                resposta.append(res)
                perguntarNovamente = False

    b, c = resposta[0], resposta[1]
    a = a
    delta = delta(a,b,c)
    raizes = raizes(a,b,c,delta['delta'])

    if delta['delta']<0:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função não apresenta uma raiz real!")
        print()
    elif delta['delta']==0:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função apresenta uma raiz reais: %.2f"%raizes['x1'])
    else:
        print()
        print("- Delta: %.2f"%delta['delta'])
        print("- Raízes: Essa função apresenta duas raízes reais: %.2f e %.2f"%(raizes['x1'], raizes['x2']))

    laco += 1