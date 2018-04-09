#!/usr/bin/python
#
# CODE BY: Diego Vinicius de Mello Munhoz
# Fatec Carapicuiba - Desenvolvimento de Jogos Digitais
#
# Servidor de Mensagens: trocar de mensagens servidor/cliente
# Módulo CHAT de comunicação
#

import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 12221
s.bind((host, port))

s.listen(5)

print("[Aguardando por conexao...]")
c, addr = s.accept()
os.system("cls")    
print("Conectado com:", addr)

while True:
    print("[Aguardando por resposta...]")
    msg = c.recv(1024)
    print("[Mensagem Recebida.........]", msg.decode("utf-8"))
    q = input("[Digite a mensagem........:] ")
    if (q == 'cls') or (q == 'CLS'):
        os.system("cls")
        print("Conectado com:", addr)
        q = input("[Digite a mensagem........:] ")
    bytes_text = bytes(q, 'utf-8')
    c.send(bytes_text)
