# Criando o codigo do servidor
import socket
from threading import Thread
L=[]

def ConversaSimultanea(a,b):
    mensagem = ""
    while mensagem != "Fim":
        print("entrou no loop da conversa")
        mensagem = L[a].recv(5000)
        if not mensagem:
            break
        L[b].sendall(mensagem)
    conn.close()

#h = raw_input("Entre com o IP do Servidor local: ")
#port = input("Entre com a Porta do Servidor local: ")

h = '127.0.0.1'
port = int('40000')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("chegou ate aqui")
s.bind((h, port))  # liga o socket com IP e porta
s.listen(1)  # espera chegar pacotes na porta especificada
print("server escutando")

for i in range(2):
    print("esperando o primeiro cliente conectar-se")
    conn, addr = s.accept()  # as variaveis conn a addr sao preenchidas pela funcao accept
    L.append(conn)
    print("conectei e appendei o primeiro cliente")
t1 = Thread(target=ConversaSimultanea, args=(1,0,)).start()
t2 = Thread(target=ConversaSimultanea, args=(0,1,)).start()