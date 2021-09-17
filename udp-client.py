import socket

HOST = 'localhost' # 127.0.0.1
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)

# msg = input('Digite a mensagem: ')

while(True):
    mensagem = bytes(input('Digite a mensagem: '), encoding='utf-8')
    udp.sendto(mensagem, destino)

udp.close()