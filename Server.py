import socket, time, struct, threading,sys

class Server():
    
    intPack = '!I' # port+3playernum+1, strings are port+3playernum+2
    boolPack = '!?' # port+3playernum
    playerIPNum = []
    numPlayers = 1
    myIP = socket.gethostbyname(socket.gethostname())
    generalSCPort = 50966
    generalCSPort = 50967
    gameStarted = False
    isRecieving = True # while true, all threads will try to recieve from all players
    recvStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rSp = 50000
    sendStr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sSp = 50001
    shouldSend = False
    sendS = ''
    target = -1
    rcvdStrs = []
    rcvdInts = []

    def __init__(self): # Begins normal broadcast of ip address to other possible players upon initialization
        collectionThread = threading.Thread(target = self.gatherPlayers,daemon = True)
        collectionThread.start()
    
    def startGame(self): # Begins the game and informs all other players
        self.gameStarted = True
        time.sleep(.5)
        if len(self.playerIPNum) > 0:
            for i in range(len(self.playerIPNum)):
                time.sleep(.1)
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

    def gatherPlayers(self, port = generalCSPort, buf_size = 1024):
        broadcastaddr = socket.inet_ntoa(socket.inet_aton(self.myIP)[:3] + b'\xff' )
        addr = ('137.112.104.246', self.generalSCPort)

        so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        so.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcast

        data = str.encode(self.myIP)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setblocking(0)
        s.settimeout(.1)
        s.bind(('', port))
        while not self.gameStarted:
            so.sendto(data, addr)
            x = time.clock() + 1
            while x > time.clock():
                try:
                    data, sender_addr = s.recvfrom(buf_size)
                    if data != None:
                        self.playerIPNum.append(sender_addr[0])
                        self.numPlayers += 1
                        self.rcvdStrs.append('')
                        self.rcvdInts.append(-1)
                except socket.error:
                    pass
        s.close()
        so.close()
        self.initThreads()

    def initThreads(self):
        self.sendStr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvStr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvStr.bind(('', self.rSp))
        self.recvStr.settimeout(.01)
        self.recvStr.setblocking(False)
        recvThread = (threading.Thread(target = self.recieving, args = ('s', self.recvStr, ''), daemon = True))
        recvThread.start()

    def sendStrToPlayer(self, data, playerNum):
        self.shouldSend = True
        self.target = playerNum
        self.sendS = data

    def recieving(self, dataType, sock, pack, buf_size = 1024):
        while self.isRecieving:
            x = time.clock() + .0001
            playerNum = -1
            if self.shouldSend:
                self.sendStr.sendto(str.encode(self.sendS), (self.playerIPNum[self.target], self.sSp))
                self.shouldSend=False
            while x > time.clock():
                try:
                    data, sender_addr = sock.recvfrom(buf_size)
                    for i in range(len(self.playerIPNum)):
                        if sender_addr == self.playerIPNum[i]:
                            playerNum = i
                    self.rcvdStrs[playerNum] = data.decode()
                    try:
                        int(self.rcvdStrs[playerNum])
                        self.rcvdInts[playerNum] = int(self.rcvdStrs[playerNum])
                    except ValueError:
                        pass
                    if self.rcvdStrs[playerNum] == 'quit':
                        del self.playerIPNum[playerNum]
                        del self.rcvdStrs[playerNum]
                        del self.rcvdInts[playerNum]
                        break
                except socket.error:
                    pass
    def endGame(self):
        for i in range(len(self.playerIPNum)):
            self.sendStrToPlayer('quit', i)