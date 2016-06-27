import socket, time, struct, threading

class Client():
    
    intPack = '!I'
    boolPack = '!?'
    serverIP = ''
    generalSCPort = 50966
    generalCSPort = 50967
    gameStarted = False
    isRecieving = True # while true, all threads will try to recieve from all players
    recvThread = []
    recvBoo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rBp = 40000
    recvInt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rIp = 40001
    recvStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rSp = 40002
    sendBoo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sBp = 50000
    sendInt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sIp = 50001
    sendStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sSp = 50002
    rcvdBool = False
    rcvdInt = -1
    rcvdStr = ''

    def __init__(self):
        self.connectWithServer()

    def connectWithServer(self, port = generalSCPort, buf_size = 1024):
        # Receive the data
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        data, sender_addr = s.recvfrom(buf_size)
        self.serverIP = sender_addr
        s.close()

    def waitForStart(self):
        initThreads()
        while not self.gameStarted:
            if self.rcvdStr == 'start':
                self.gameStarted = True

    def initThreads(self):
        self.recvBoo.bind(('', self.rBp))
        self.recvInt.bind(('', self.rIp))
        self.recvStr.bind(('', self.rSp))
        self.recvBoo.settimeout(.1)
        self.recvBoo.setblocking(0)
        self.recvInt.settimeout(.1)
        self.recvInt.setblocking(0)
        self.recvStr.settimeout(.1)
        self.recvStr.setblocking(0)
        recvThread.append(threading.Thread(target = recieving, args = ('b', self.recvBoo, self.boolPack), daemon = True))
        recvThread.append(threading.Thread(target = recieving, args = ('i', self.recvInt, self.intPack), daemon = True))
        recvThread.append(threading.Thread(target = recieving, args = ('s', self.recvStr, ''), daemon = True))
        recvThread[0].start()
        recvThread[1].start()
        recvThread[2].start()
    
    def recieving(self, dataType, sock, pack, buf_size = 1024):
        while self.isRecieving:
            x = time.clock() + .01
            while time.clock() < x:
                data, sender_addr = sock.recvfrom(buf_size)
                if dataType == 'b':
                    self.rcvdBool = struct.unpack(pack, data)[0]
                elif dataType == 'i':
                    self.rcvdInt = struct.unpack(pack,data)[0]
                else:
                    self.rcvdStr = data.decode()
                    if self.rcvdStr == 'quit':
                        sys.exit
    
    def getInt(self):
        return self.rcvdInt

    def getBool(self):
        return self.rcvdBool

    def getStr(self):
        return self.rcvdStr
    
    def sendBoolToServer(self, data):
        self.sendBoo.sendto(struct.pack(self.boolPack, data), (self.serverIP, self.sBp))
    
    def sendIntToServer(self, data):
        self.sendInt.sendto(struct.pack(self.intPack, data), (self.serverIP, self.sIp))

    def sendStrToServer(self, data):
        self.sendStr.sendto(str.encode(data), (self.serverIP, self.sSp))