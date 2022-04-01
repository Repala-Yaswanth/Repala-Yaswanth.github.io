import socket
from threading import *
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8000
ServerSocket.bind((host, port))


class Client (Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r = input('Send data -->')
            ClientSocket.send(r.encode())
            print(ClientSocket.recv(1024).decode())


ServerSocket.listen(5)
print('Sender ready and is listening')
while True:
    # To accept all incoming connections
    ClientSocket, Address = ServerSocket.accept()
    print('Receiver' + str(Address) + 'connected')
    Client(ClientSocket, Address)
