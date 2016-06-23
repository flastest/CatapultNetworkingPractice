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
        waitForStart()

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
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdBool, self.recvBoo, self.boolPack, False)))
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdInt, self.recvInt, self.intPack, False)))
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdStr, self.recvStr, '', True)))
        recvThread[0].start()
        recvThread[1].start()
        recvThread[2].start()
    
    def recieving(self, dataStorage, sock, pack, isStr, buf_size = 1024):
        while self.isRecieving:
            playerNum = -1
            x = time.clock() + .01
            while time.clock() < x:
                data, sender_addr = sock.recvfrom(buf_size)
                for i in range(len(self.playerIPNum)):
                    if sender_addr == self.playerIPNum[i]:
                        playerNum = i
                if not isStr:
                    self.dataStorage[playerNum] = struct.unpack(pack, data)[0]
                else:
                    self.dataStorage[playerNum] = data.decode()
    
    def sendBoolToServer(self, data):
        self.sendBoo.sendTo(struct.pack(self.boolPack, data), (self.serverIP, self.sBp))
    
    def sendIntToServer(self, data):
        self.sendInt.sendTo(struct.pack(self.intPack, data), (self.serverIP, self.sIp))

    def sendStrToServer(self, data):
        self.sendStr.sendTo(str.encode(data), (self.serverIP, self.sSp))