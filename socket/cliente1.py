#!/usr/bin/python
# Coded by: Diego Munhoz
#

import socket

ip = input('digite o ip de conexao: ')
port = 7000
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = input("digite uma mensagem para enviar ao servidor")
bytes_text = bytes(mensagem, 'utf-8')
client_socket.send(bytes_text)
print ('mensagem enviada')
client_socket.close()