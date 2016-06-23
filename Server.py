import socket, time, struct, threading

class Server: # player number will always be output to players classes as 2 less than the actual value that should be shown, ie host will be -1, this is done so that the data may be stored and accessed from the server more easily.
    
    intPack = '!I' # port+3playernum+1, strings are port+3playernum+2
    boolPack = '!?' # port+3playernum
    playerIPNum = []
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
    rcvdBools = []
    rcvdInts = []
    rcvdStrs = []

    def __init__(self): # Begins normal broadcast of ip address to other possible players upon initialization
        self.broadcast()
    
    def startGame(self): # Begins the game and informs all other players
        self.gameStarted = True
        for i in range(len(self.playerIPNum)):
            self.sendStrToPlayer('start', i)

    def backupBroadcast(self, port = generalSCPort): # only run this if on a massive wifi system, with more than 200 computers on it, if broadcast doesnt work
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
                        s.sendto(str.encode(myIP), ((privateNetworkPartialIP + str(x) + '.' + str(y)), port))
        s.close()

    def broadcast(self, port = generalSCPort): # 
        collectionThread = threading.Thread(target = self.gatherPlayers)
        collectionThread.start()
        
        broadcastaddr = socket.inet_ntoa(socket.inet_aton(self.myIP)[:3] + b'\xff' )
        addr=(broadcastaddr, port)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcasr

        data=self.myIP

        #s.bind(('', port))
        s.sendto(str.encode(data), addr)
        s.close()

    def gatherPlayers(self, port = generalCSPort, buf_size = 1024):  # runs during setup, gathers and organizes the other players ip addresses into global list playerIPNum, and sends the players their player number - 2
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        while not self.gameStarted:
            count = len(self.playerIPNum)
            shouldAdd = True
            data, sender_addr = s.recvfrom(buf_size)
            for x in range(len(self.playerIPNum)):
                if sender_addr == self.playerIPNum[i]:
                    shouldAdd = False
            if shouldAdd:
                self.playerIPNum.append(sender_addr) # adds players IP num
                self.sendIntToPlayer(count, count) # sends the player their player number
        for i in range(len(self.playerIPNum)):
            self.rcvdBools.append(False)
            self.rcvdInts.append(-1)
            self.rcvdStrs.append('')
        self.initThreads()

    def initThreads(self): # initializes the threads that are constantly recieving data from the other players, uses the recieving function.
        self.recvBoo.bind(('', self.rBp))
        self.recvInt.bind(('', self.rIp))
        self.recvStr.bind(('', self.rSp))
        self.recvBoo.settimeout(.1)
        self.recvBoo.setblocking(0)
        self.recvInt.settimeout(.1)
        self.recvInt.setblocking(0)
        self.recvStr.settimeout(.1)
        self.recvStr.setblocking(0)
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdBools[count], self.recvBoo, self.boolPack, False)))
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdInts[count], self.recvInt, self.intPack, False)))
        recvThread.append(threading.Thread(target = recieving, args = (self.rcvdStrs[count], self.recvStr, '', True)))
        recvThread[0].start()
        recvThread[1].start()
        recvThread[2].start()

    def sendBoolToPlayer(self, data, playerNum): # data = boolean being sent
        self.sendBoo.sendTo(struct.pack(self.boolPack, data), (self.playerIPNum[playerNum], self.sBp))
    
    def sendIntToPlayer(self, data, playerNum): # data = int being sent
        self.sendInt.sendTo(struct.pack(self.intPack, data), (self.playerIPNum[playerNum], self.sIp))

    def sendStrToPlayer(self, data, playerNum): # data = str being sent
        self.sendStr.sendTo(str.encode(data), (self.playerIPNum[playerNum], self.sSp))

    def recieving(self, dataStorage, sock, pack, isStr, buf_size = 1024): # actively recieves from all players, determines which player sent the data and stores it in the player's number location in the global list corresponding to the data type
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