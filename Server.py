import socket, time, struct, threading

class Server:
    
    intPack = '!I'
    boolPack = '!?'
    playerIPNum = []
    myIP = socket.gethostbyname(socket.gethostname())
    generalSCPort = 50966
    generalCSPort = 50967
    gameStarted = False
    socketToPlayer = []
    socketFromPlayer = []
    recvThread = []

    def __init__(self):
        self.broadcast()
    
    def backupBroadcast(self, port = self.generalSCPort):
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

    def broadcast(self, port = self.generalSCPort):
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

    def gatherPlayers(self, port = self.generalCSPort, buf_size = 1024):
        count = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        while not self.gameStarted:
            data, sender_addr = s.recvfrom(buf_size)
            playerIPNum[count] = sender_addr[0]
            socketToPlayer[count] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socketFromPlayer[count] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socketFromPlayer[count].bind(('', 4000+count))
            socketFromPlayer[count].settimeout(.1)
            socketFromPlayer[count].setblocking(0)
            recvThread[count] = socketFromPlayer

    def sendToPlayer(self, playerNum)