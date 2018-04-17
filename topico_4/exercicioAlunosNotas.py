# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Exercícios Alunos x Notas                                                                    ******
# ******             a) Crie uma matriz 2D p/ guardar notas de 10 alunos, sendo que o ano letivo possui 5 notas   ******
# ******             b) Crie um código para pedir para o usuário digitar as notas de cada aluno e guarde as       ******
# ******                informações na posição correspondente da matriz                                           ******
# ******             c) Crie um código para exibir as notas dos alunos na tela                                    ******
# ******             d) Informe qual é a maior nota digitada                                                      ******
# ******             e) Informe qual é a menor nota digitada                                                      ******
# ******             f) Calcule a média de cada aluno                                                             ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 17/04/2018                                                                                   ******
# **********************************************************************************************************************

import statistics

# Método para capturar os dados informados pelo usuario e montar a matriz 2D
def montar_matriz():
    for x in range(10):
        notas.append([])
        for y in range(5):
            invalido = True
            while invalido:
                try:
                    nota = int(input(("Informe a {}ª nota do {}° aluno:").format(y + 1, x + 1)))
                    if (nota < 0) or (nota > 10):
                        print("A nota deve estar entre 0 <ZERO> e 10 <DEZ>!")
                        invalido = True
                    else:
                        invalido = False
                except ValueError:
                    print("Informe uma nota valida!")
                    continue
            notas[x].append(nota)

# Método para separar as notas para cada aluno
def separa_notas(matriz):
    aluno = 0
    for linha in matriz:
        aluno += 1
        for coluna in linha:
            if (aluno == 1):
                notas_aluno1.append(coluna)
            elif (aluno == 2):
                notas_aluno2.append(coluna)
            elif (aluno == 3):
                notas_aluno3.append(coluna)
            elif (aluno == 4):
                notas_aluno4.append(coluna)
            elif (aluno == 5):
                notas_aluno5.append(coluna)
            elif (aluno == 6):
                notas_aluno6.append(coluna)
            elif (aluno == 7):
                notas_aluno7.append(coluna)
            elif (aluno == 8):
                notas_aluno8.append(coluna)
            elif (aluno == 9):
                notas_aluno9.append(coluna)
            else:
                notas_aluno10.append(coluna)
    notas_aluno1.sort()
    notas_aluno2.sort()
    notas_aluno3.sort()
    notas_aluno4.sort()
    notas_aluno5.sort()
    notas_aluno6.sort()
    notas_aluno7.sort()
    notas_aluno8.sort()
    notas_aluno9.sort()
    notas_aluno10.sort()

# Método para exibir notas digitadas
def exibir_notas(matriz):
    aluno = 0
    print('\nNotas cadastradas de cada aluno:')
    for linha in matriz:
        nota = 0
        aluno += 1
        for coluna in linha:
            nota += 1
            print(('{}ª nota do {}° aluno: {}').format(nota,aluno,coluna))

# Método para exibir a maior nota de cada aluno
def maior_nota():
    print('\nLista das maiores notas por aluno:')
    print('Maior nota do 1º aluno:', notas_aluno1[(len(notas_aluno1) - 1)])
    print('Maior nota do 2º aluno:', notas_aluno2[(len(notas_aluno2) - 1)])
    print('Maior nota do 3º aluno:', notas_aluno3[(len(notas_aluno3) - 1)])
    print('Maior nota do 4º aluno:', notas_aluno4[(len(notas_aluno4) - 1)])
    print('Maior nota do 5º aluno:', notas_aluno5[(len(notas_aluno5) - 1)])
    print('Maior nota do 6º aluno:', notas_aluno6[(len(notas_aluno6) - 1)])
    print('Maior nota do 7º aluno:', notas_aluno7[(len(notas_aluno7) - 1)])
    print('Maior nota do 8º aluno:', notas_aluno8[(len(notas_aluno8) - 1)])
    print('Maior nota do 9º aluno:', notas_aluno9[(len(notas_aluno9) - 1)])
    print('Maior nota do 10º aluno:', notas_aluno10[(len(notas_aluno10) - 1)])

# Método para exibir a menor nota de cada aluno
def menor_nota():
    print('\nLista das menores notas por aluno:')
    print('Menor nota do 1º aluno:', notas_aluno1[0])
    print('Menor nota do 2º aluno:', notas_aluno2[0])
    print('Menor nota do 3º aluno:', notas_aluno3[0])
    print('Menor nota do 4º aluno:', notas_aluno4[0])
    print('Menor nota do 5º aluno:', notas_aluno5[0])
    print('Menor nota do 6º aluno:', notas_aluno6[0])
    print('Menor nota do 7º aluno:', notas_aluno7[0])
    print('Menor nota do 8º aluno:', notas_aluno8[0])
    print('Menor nota do 9º aluno:', notas_aluno9[0])
    print('Menor nota do 10º aluno:', notas_aluno10[0])

# Método para exibir a média de cada aluno
def media_nota():
    print('\nMédia de notas de cada aluno:')
    print('Média do 1º aluno:', statistics.mean(notas_aluno1))
    print('Média do 2º aluno:', statistics.mean(notas_aluno2))
    print('Média do 3º aluno:', statistics.mean(notas_aluno3))
    print('Média do 4º aluno:', statistics.mean(notas_aluno4))
    print('Média do 5º aluno:', statistics.mean(notas_aluno5))
    print('Média do 6º aluno:', statistics.mean(notas_aluno6))
    print('Média do 7º aluno:', statistics.mean(notas_aluno7))
    print('Média do 8º aluno:', statistics.mean(notas_aluno8))
    print('Média do 9º aluno:', statistics.mean(notas_aluno9))
    print('Média do 10º aluno:', statistics.mean(notas_aluno10))

# Lista 2D que irá armazenar as notas dos alunos
notas = []

# Lista para separar as notas de cada aluno
notas_aluno1 = []
notas_aluno2 = []
notas_aluno3 = []
notas_aluno4 = []
notas_aluno5 = []
notas_aluno6 = []
notas_aluno7 = []
notas_aluno8 = []
notas_aluno9 = []
notas_aluno10 = []

if __name__ == '__main__':
    montar_matriz()
    separa_notas(notas)
    exibir_notas(notas)
    maior_nota()
    menor_nota()
    media_nota()