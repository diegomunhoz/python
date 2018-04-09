#!/usr/bin/env python3
# Programa para testar a função format()

s = 'Adoro Python'

# alinha a direita com 20 espaços em branco
print("{0:>20}".format(s))

# alinha a direita com 20 símbolos #
print("{0:#>20}".format(s))

# alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
print("{0:^20}".format(s))

# imprime só as primeiras cinco letras
print("{0:.5}".format(s))