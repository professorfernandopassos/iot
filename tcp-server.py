import socket

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
tcp.bind(origem)
tcp.listen(1)
print('Serviço iniciado. ')

while(True):
    con, cliente = tcp.accept()
    print('Conectado por ', cliente)
    while(True):
        mensagem = con.recv(1024)
        print(cliente, mensagem)

con.close()