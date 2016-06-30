import socket, time, struct, threading

class Client():
    
    intPack = '!I'
    boolPack = '!?'
    serverIP = ''
    generalSCPort = 50966
    generalCSPort = 50967
    gameStarted = False
    isRecieving = True # while true, all threads will try to recieve from all players
    recvStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rSp = 50001
    sendStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sSp = 50000
    shouldAnswer = False
    isConnected = False
    shouldSend = False
    sendS = ''
    rcvdStr = ''

    def __init__(self):
        t = threading.Thread(target = self.connectWithServer, daemon = True)
        t.start()

    def connectWithServer(self, port = generalSCPort, buf_size = 1024):
        # Receive the data
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(0)
        s.settimeout(.1)
        s.bind(('', port))
        so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        y = time.clock()+.01
        while not self.isConnected:
            while y < time.clock():
                y = time.clock()+.001
                if self.shouldAnswer:
                    try:
                        so.sendto(data, (self.serverIP, self.generalCSPort))
                        self.isConnected = True
                    except socket.error:
                        pass
                else:
                    try:
                        data, sender_addr = s.recvfrom(buf_size)
                        if data != None:
                            self.serverIP = sender_addr[0]
                            self.shouldAnswer = True
                    except socket.error:
                        pass
        print('Connected!!!')
        self.initThreads()
        

    def waitForStart(self):
        if self.rcvdStr == 'start':
            self.gameStarted = True

    def initThreads(self):
        self.recvStr.bind(('', self.rSp))
        self.recvStr.settimeout(.1)
        self.recvStr.setblocking(0)
        recvThread = (threading.Thread(target = self.recieving, args = (self.recvStr), daemon = True))
        recvThread.start()
    
    def recieving(self, sock, buf_size = 1024):
        while self.isRecieving:
            x = time.clock() + .0001
            if self.shouldSend:
                self.sendStr.sendto(str.encode(self.sendS), (self.serverIP, self.sSp))
                self.shouldSend=False
            while x > time.clock():
                try:
                    self.rcvdStr = data.decode()
                except socket.error:
                    pass
                if self.rcvdStr == 'quit':
                    sys.exit

    def sendStrToServer(self, data):
        self.shouldSend = True
        self.sendS = data