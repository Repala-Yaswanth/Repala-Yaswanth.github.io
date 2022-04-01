import socket
from threading import *
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 5555
s.bind((host, port))


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run (self):
        while True:
            bitstring = str(input(('Enter bit string :')))
            propogationtime = 1
            p_nosend = 0.2
            l=[]
            for i in range(0,1000):
                l = l + [i]
            i=0
            while(i < len(bitstring)):
                datadict = {}
                datadict = {i%2: bitstring[i],}
                sendstring = str (datadict)
                number = random.randint(0,1000)
                time1 = time.time()
                if l[number] < (p_nosend * 1000):
                    clientsocket.send(sendstring.encode())
                    time.sleep((propogationtime) / 1.1)
                    time2 = time.time()
                    ackflag = False
                else :
                    time.sleep(propogationtime / 1.1)
                    time2 = time.time()
                    print("package dropped 1")
                    ackflag = False


                while (True):
                    if ((time2 - time1) <= propogationtime):
                        time2 = time.time()
                        clientsocket.settimeout(propogationtime / 1.1)

                    try:
                        recieved = clientsocket.recv(1024).decode()
                        print(recieved)

                        if recieved:
                            print("ack received")
                            i = i + 1
                            ackflag = True
                            break

                    except :
                        if ((time2 - time1) > propogationtime and ackflag == False):
                            print("timeout")
                            number = random.randint(0, 1000)

                            if l[number] < (p_nosend * 1000):
                                clientsocket.send(sendstring.encode())
                                time1 = time.time()
                                time2 = time.time()
                                print("package sent")
                            else:
                                time1 = time.time()
                                time2 = time.time()
                                print('package dropped 2')


s.listen(5)
print('Sender ready and is listening')
while(True):
    #To accept all incoming connections
    clientsocket , address = s.accept()
    print('Receiver'+ str(address)+ 'connected')
    client(clientsocket,address)



