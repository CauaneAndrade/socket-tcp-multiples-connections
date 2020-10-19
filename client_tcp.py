import socket  # Cliente TCP


SERVER = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5002  # Porta que o Servidor esta escutando
tcp = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
dest = (SERVER, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send(msg.encode())
    msg = input()
tcp.close()

u"""
Em tcp.connect(dest), o método connect recebe o IP e a porta do servidor que vai se conectar.
E em tcp.send(data.encode()) o send envia os pacotes que o cliente envia para o servidor.
"""