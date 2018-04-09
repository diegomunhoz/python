import socket
from threading import Thread
def client(h, p):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        try:
            s.connect((h, p))
            break
        except Exception as e:
            pass

    print("Conectou")
    msg = ''
    while msg != "Fim":
        msg = raw_input("Entre com a mensagem: ")
        s.sendall(msg)# Envia dados
        var = s.recv(1024)
        print(var)
    s.close()  # Termina conexao
    print("Fechou a conexao")
if __name__ == '__main__':

    h2 = input("Entre com o IP do servidor remoto:")
    port2= input("Entre com a porta do servidor remoto:")
    client(h2,port2)