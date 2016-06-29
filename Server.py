import socket, time, struct, threading

class Server:
    
    intPack = '!I' # port+3playernum+1, strings are port+3playernum+2
    boolPack = '!?' # port+3playernum
    playerIPNum = []
    numPlayers = 1
    myIP = socket.gethostbyname(socket.gethostname())
    generalSCPort = 50966
    generalCSPort = 50967
    gameStarted = False
    isRecieving = True # while true, all threads will try to recieve from all players
    recvThread = []
    recvBoo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rBp = 50000
    recvInt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rIp = 50001
    recvStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rSp = 50002
    sendBoo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sBp = 40000
    sendInt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sIp = 40001
    sendStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sSp = 40002
    shouldSendB = False
    shouldSendI = False
    shouldSendS = False
    sendB = False
    sendI = -1
    sendS = ''
    target = -1
    rcvdBools = []
    rcvdInts = []
    rcvdStrs = []

    def __init__(self): # Begins normal broadcast of ip address to other possible players upon initialization
        collectionThread = threading.Thread(target = self.gatherPlayers, daemon = True)
        broadcastingThread = threading.Thread(target = self.broadcastThread, daemon = True)
        collectionThread.start()
        broadcastingThread.start()
    
    def startGame(self): # Begins the game and informs all other players
        self.gameStarted = True
        print(str(len(self.playerIPNum)))
        if len(self.playerIPNum) >= 0:
            for i in range(len(self.playerIPNum)):
                self.sendStrToPlayer('start', i)

    def backupBroadcast(self, port = generalSCPort):
        count = 0
        privateNetworkPartialIP = ''
        for i in range(len(self.myIP)):
            if self.myIP[i] == '.':
                count += 1
            if count == 2:
                privateNetworkPartialIP = self.myIP[:i+1]
                count += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for x in range(256):
            for y in range(256):
                s.sendto(str.encode(self.myIP), ((privateNetworkPartialIP + str(x) + '.' + str(y)), port))
        s.close()

    def getPlayerCount(self):
        return self.numPlayers

    def broadcast(self, port = generalSCPort):
        broadcastaddr = socket.inet_ntoa(socket.inet_aton(self.myIP)[:3] + b'\xff' )
        addr=(broadcastaddr, port)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcast

        data = self.myIP

        s.bind(('', port))
        while not self.gameStarted:
            x = time.clock() + .0001
            while x > time.clock():
                s.sendto(str.encode(data), addr)

    def gatherPlayers(self, port = generalCSPort, buf_size = 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(0)
        s.settimeout(.1)
        s.bind(('', port))
        while self.numPlayers < 15 and not self.gameStarted:
            try:
                data, sender_addr = s.recvfrom(buf_size)
                self.playerIPNum.append(sender_addr)
                self.numPlayers+=1
                print('got one!')
            except socket.error:
                pass
        for i in range(len(self.playerIPNum)):
            self.rcvdBools.append(False)
            self.rcvdInts.append(-1)
            self.rcvdStrs.append('')
        self.initThreads()

    def initThreads(self):
        self.recvBoo.bind(('', self.rBp))
        self.recvInt.bind(('', self.rIp))
        self.recvStr.bind(('', self.rSp))
        self.recvBoo.settimeout(.01)
        self.recvBoo.setblocking(False)
        self.recvInt.settimeout(.01)
        self.recvInt.setblocking(False)
        self.recvStr.settimeout(.01)
        self.recvStr.setblocking(False)
        self.recvThread.append(threading.Thread(target = self.recieving, args = ('b', self.recvBoo, self.boolPack), daemon = True))
        self.recvThread.append(threading.Thread(target = self.recieving, args = ('i', self.recvInt, self.intPack), daemon = True))
        self.recvThread.append(threading.Thread(target = self.recieving, args = ('s', self.recvStr, ''), daemon = True))
        self.recvThread[0].start()
        self.recvThread[1].start()
        self.recvThread[2].start()

    def sendBoolToPlayer(self, data, playerNum):
        self.shouldSendB = True
        self.target = playerNum
        self.sendB = data
    
    def sendIntToPlayer(self, data, playerNum):
        self.shouldSendB = True
        self.target = playerNum
        self.sendB = data

    def sendStrToPlayer(self, data, playerNum):
        self.shouldSendB = True
        self.target = playerNum
        self.sendB = data

    def recieving(self, dataType, sock, pack, buf_size = 1024):
        while self.isRecieving:
            x = time.clock() + .0001
            playerNum = -1
            if self.shouldSendB and dataType == 'b':
                self.sendBoo.sendto(struct.pack(self.boolPack, self.sendB), (self.playerIPNum[self.target], self.sBp))
                self.shouldSendB = False
            if self.shouldSendI and dataType == 'i':
                self.sendInt.sendto(struct.pack(self.intPack, self.sendI), (self.playerIPNum[self.target], self.sIp))
                self.shouldSendI = False
            if self.shouldSendS and dataType == 's':
                self.sendStr.sendto(str.encode(self.sendS), (self.playerIPNum[self.target], self.sSp))
                self.shouldSendS=False
            while x > time.clock():
                try:
                    data, sender_addr = sock.recvfrom(buf_size)
                    for i in range(len(self.playerIPNum)):
                        if sender_addr == self.playerIPNum[i]:
                            playerNum = i
                    if dataType == 'b':
                        self.rcvdBools[playerNum] = struct.unpack(pack, data)[0]
                    elif dataType == 'i':
                        self.rcvdInts[playerNum] = struct.unpack(pack,data)[0]
                    else:
                        self.rcvdStrs[playerNum] = data.decode()
                        if self.rcvdStrs[playerNum] == 'quit':
                            del self.playerIPNum[playerNum]
                            del self.rcvdBools[playerNum]
                            del self.rcvdInts[playerNum]
                            del self.rcvdStrs[playerNum]
                            break
                except socket.error:
                    print(socket.error)
    def endGame(self):
        for i in range(len(self.playerIPNum)):
            self.sendStrToPlayer('quit', i)
    def broadcastThread(self):
        self.broadcast()