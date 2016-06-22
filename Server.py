import socket, time, struct, threading

class Server:
    
    intPack = '!I'
    boolPack = '!?'
    playerIPNum = []
    myIP = socket.gethostbyname(socket.gethostname())
    generalPort = 50966
    playerPort = []
    myPort = []

    def __init__(self):
        self.broadcast()
    
    def backupBroadcast(self, port = self.generalPort):
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

    def broadcast(self, port = self.generalPort):
        host = ''                               # Bind to all interfaces
        broadcastaddr = socket.inet_ntoa(socket.inet_aton(self.myIP)[:3] + b'\xff' )
        addr=(broadcastaddr, port)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)   #broadcasr

        data=myip

        s.bind(('', port))                  #socket binding to any host
        s.sendto(str.encode(data), addr)
        s.close()