import socket

HOST = ''
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = (HOST, PORT)
udp.bind(origem)

print("Serviço UDP inicializado. Aguardando mensagem. \n")

while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg)

udp.close()

