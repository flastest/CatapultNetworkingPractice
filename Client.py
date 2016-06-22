import socket, time, struct, threading

class Client():
    
    intPack = '!I'
    boolPack = '!?'
    myIP = socket.gethostbyname(socket.gethostname())
    serverIP = ''
    generalSCPort = 50966
    generalCSPort = 50967
    serverPort = []
    myPort = []

    def __init__(self):
        self.connectWithServer()

    def connectWithServer(self, port = self.generalSCPort, buf_size = 1024):
        # Receive the data
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        data, sender_addr = s.recvfrom(buf_size)
        s.close()