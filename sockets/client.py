import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.0.209',4000))

while True:
    mensagem = input('Enter mensage: ')
    c.send(mensagem.encode("utf-8")[:2048])
    