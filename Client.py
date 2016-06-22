import socket, time, struct, threading

class Client():
    
    myIP = socket.gethostbyname(socket.gethostname())
    serverIP = ''
    generalPort = 50966
    serverPort = []
    myPort = []

    def __init__(self):
        self.recieve()

    def recieve(self, port):
