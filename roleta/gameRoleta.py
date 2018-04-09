# Desenvolvedor: Diego Vinicius de Mello Munhoz
#
# Exercício: Jogo da Roleta
#
# Crie um jogo de roleta, onde o computador solicitará ao jogador como será feita a aposta e quanto deseja apostar.
#
# Regras:
#  • O jogador começa com R$ 1.000,00 e a banca possui R$ 5.000,00 iniciais
#  • O jogo termina quando o jogador ficar com um valor <= R$ 0,00 indicando derrota, ou quando a banca ficar com um valor <= a R$ 0,00 indicando vitória do jogador.
#
# No início de cada rodada o jogador deve escolher qual será o tipo de aposta, uma das opções abaixo:
# 1 - Apostar no Par
# 2 - Apostar no Impar
# 3 - Apostar em um número específico (não pode apostar no número 0)
#
import random

saldoJogador = 1000
saldoBanca = 5000
saldoAposta = 0
fimJogo = 'N'

#
# FUNÇÃO UTILIZANDO MEDIA PONDERADA PARA FACILITAR O RESULTADO DO VALOR '0 (ZERO)'
# NO SORTEIO EFETUADO ENTRE OS VALORES (0-36)
#
def sorteio():
    w_prizes = [('0', 2), ('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1), ('7', 1), ('8', 1),
                ('9', 1),  ('10', 1), ('11', 1), ('12', 1), ('13', 1), ('14', 1), ('15', 1), ('16', 1), ('17', 1),
                ('18', 1), ('19', 1), ('20', 1), ('21', 1), ('22', 1), ('23', 1), ('24', 1), ('25', 1), ('26', 1), ('27', 1),
                ('28', 1), ('29', 1), ('30', 1), ('31', 1), ('32', 1), ('33', 1), ('34', 1), ('35', 1), ('36', 1)]
    prize_list = [prize for prize, weight in w_prizes for i in range(weight)]
    return int(random.choice(prize_list))

#
# FUNÇÃO RESPONSÁVEL POR PROCESSAR O RESULTADO DA APOSTA
# A FUNÇÃO RECEBE O TIPO DA APOSTA, NUM SORTEADO NA ROLETA E VALOR APOSTADO PELO JOGADOR
#
def processarResultado(str_tipoAposta, str_numRoleta, str_apostaValor):

    #PROCESSAMENTO PARA APOSTA EM VALOR PAR
    if(str_tipoAposta == 1):
        if(str_numRoleta  == 0):
            print("Numero Sorteado: ", str_numRoleta)
            str_apostaValor = -saldoJogador
            return str_apostaValor
        elif(str_numRoleta  % 2 == 0):
            str_apostaValor *= 2
            print("Numero Sorteado: ", str_numRoleta)
            print("Você acertou, ganhou R$ ", str_apostaValor)
            return str_apostaValor
        else:
            print("Numero Sorteado: ", str_numRoleta)
            print("Você errou, perdeu R$ ", str_apostaValor)
            str_apostaValor = -str_apostaValor
            return str_apostaValor

    # PROCESSAMENTO PARA APOSTA EM VALOR IMPAR
    elif (str_tipoAposta == 2):
        if (str_numRoleta == 0):
            print("Numero Sorteado: ", str_numRoleta)
            str_apostaValor = -saldoJogador
            return str_apostaValor
        elif (str_numRoleta % 2 != 0):
            str_apostaValor *= 2
            print("Numero Sorteado: ", str_numRoleta)
            print("Você acertou, ganhou R$ ", str_apostaValor)
            return str_apostaValor
        else:
            print("Você errou, perdeu R$ ", str_apostaValor)
            str_apostaValor = -str_apostaValor
            return str_apostaValor

    # PROCESSAMENTO PARA APOSTA EM VALOR ESPECIFICO
    elif (str_tipoAposta == 3):
        apostaNumero = int(input("Digite o numero da aposta:"))
        if(apostaNumero == 0):
            print("O numero apostado não pode ser 0(zero)")
            return 0
        if (apostaNumero == str_numRoleta):
            str_apostaValor *= 30
            print("Numero Sorteado: ", str_numRoleta)
            print("Você acertou, ganhou R$ ", str_apostaValor)
            return str_apostaValor
        elif (str_numRoleta == 0):
            print("Numero Sorteado: ", str_numRoleta)
            print("Você perdeu tudo!!")
            str_apostaValor = -saldoJogador
            return str_apostaValor
        else:
            print("Numero Sorteado: ", str_numRoleta)
            print("Você errou, perdeu R$ ", str_apostaValor)
            str_apostaValor = -str_apostaValor
            return str_apostaValor

    # TRATAMENTO PARA OPÇÃO DE APOSTA INVALIDO
    else:
        print("Opção Inválida!")
        return 0

#
# PROCESSAMENTO DO JOGO ENQUANTO O SALDO DO JOGADOR FOR MAIOR QUE '0 (ZERO)'
# INFORMANDO O TIPO DE VALOR DA APOSTA
#
print(" *** !!!! JOGO DE ROLETA !!!! ***")
print(" ***   FATEC DE CARAPICUIBA   ***")
while (fimJogo != 'S'):

    str_apostaValor = 0
    while (str_apostaValor == 0):
        str_apostaValor = int(input("INFORME O VALOR DA APOSTA:"))
        if (str_apostaValor == 0):
            print("Valor da aposta não pode ser 0 (zero)!")

    print("INFORME O TIPO DE APOSTA:")
    print("  1 - APOSTAR NO PAR")
    print("  2 - APORTAR NO IMPAR")
    print("  3 - APOSTAR NUMERO ESPECIFICO")
    str_tipoAposta = int(input("  --> "))

    str_numRoleta = sorteio()
    saldoAposta = processarResultado(str_tipoAposta, str_numRoleta, str_apostaValor)

    if (saldoAposta != 0):
        saldoJogador += saldoAposta
        saldoBanca -= saldoAposta
        print("Saldo Jogador: R$ ", saldoJogador)
        print("Saldo Banca: R$ ", saldoBanca)

    print("")

    #VERIFICAÇÃO DO SALDO DA BANCA PARA FINALIZAÇÃO DO JOGO
    if(saldoBanca <= 0):
        print("**** Você quebrou a banca! SALDO TOTAL: R$", saldoJogador, " ****")
        fimJogo = 'S'
        break

    # VERIFICAÇÃO DO SALDO DO JOGADOR PARA FINALIZAÇÃO DO JOGO
    if(saldoJogador <= 0):
        print("!!! Você PERDEU tudo !!!")
        fimJogo = 'S'
        break