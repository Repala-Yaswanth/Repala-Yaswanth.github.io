import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8000
s.connect((host, port))

while 2:
    data = s.recv(1024).decode()
    print("Received -->"+data)
    string = "Acknowledgment : Message Received"
    s.send(string.encode())

s.close()
