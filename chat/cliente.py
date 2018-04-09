#!/usr/bin/python
#
# CODE BY: Diego Vinicius de Mello Munhoz
# Fatec Carapicuiba - Desenvolvimento de Jogos Digitais
#
# Cliente de Mensagens: trocar de mensagens cliente/servidor
# Módulo CHAT de comunicação
#

import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 12221

s.connect((host, port))
os.system("cls")
print("Conectado com:", host)

while True:
    z = input("[Digite a mensagem........:] ")

    if (z == 'cls') or (z == 'CLS'):
        os.system("cls")
        print("Conectado com:", host)
        z = input("[Digite a mensagem........:] ")

    bytes_text = bytes(z, 'utf-8')
    s.send(bytes_text)

    print("[Aguardando por resposta...]")
    msg = s.recv(1024)
    print("[Mensagem Recebida.........]", msg.decode("utf-8"))