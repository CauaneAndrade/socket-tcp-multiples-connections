# Servidor TCP
import socket
from threading import Thread


def conexao(con, cli):
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(msg)
    print('Finalizando conexao do cliente', cli)
    con.close()


# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Conectado por ', cliente)
    t = Thread(target=conexao, args=(con, cliente,))
    t.start()

u"""
Na criação do Socket, o socket.socket() pode receber até 3 parâmetros: o primeiro é a família de protocolos, o segundo é o tipo de transmissão, podendo ser TCP ou UDP; e o último parâmetro é o protocolo de transmissão (IPv4 ou IPv6). <br>
O método `tcp.bind(orig)` é utilizada apenas pelo servidor, uma vez que associa um determinado endereço IP e porta TCP para o processo servidor. <br>
Em `tcp.listen(1)` indica ao SO para colocar o socket em modo de espera para aguardar conexões de clientes, o valor `1` passado ao método define o número de conexões não aceitas que o sistema permitirá antes de recusar novas conexões. <br>

No laço `While`, O `tcp.accept()` aguarda ou bloquei uma nova conexão, quando um cliente se conecta é retornado um novo socket. <br>
Em `Thread(target=conexao, args=(con, cliente,))`, está definindo uma nova Thread que recebe como argumento o método a ser executado e uma tupla, onde é definido a conexão e o cliente. <br>
O argumento passado no target é um método que lê os dados passados pelo cliente e encerra a conexão.
"""
