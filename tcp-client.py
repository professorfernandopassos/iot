import socket

HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

tcp.connect(destino)

while(True):
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8')
    tcp.send(mensagem)

tcp.close()