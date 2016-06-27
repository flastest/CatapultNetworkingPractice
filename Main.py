# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame, random, threading 
from pygame.locals import *
from TitleScreen import *
from Server import *
from Client import *

from AntivirusProgrammer import*
from Burglar import *
from Hacker import *
from Doctor import *
from Librarian import *
#from Police import *
from Villain import *

class Main:
    numberOfClasses = 7    # CHANGE THIS AND classPicker() AS WE ADD MORE CHARACHTER CLASSES
    TIME_THAT_WE_SHOULD_HAVE_THEM_READ_THEIR_CHARACTER_INFO_FOR = 10
    atTitleScreen = True
    isLoading = False
    closed = False

    gray = [150,150,150]
    green = [34,177,76]
    blue = [63,72,204]
    pygame.init()
    mainScreens = TitleScreen()
    game_screen = pygame.display.set_mode([1200,800])
    pygame.display.set_caption("Cookie Scam")
    mainScreens.displayTitleScreen(game_screen)
    pygame.display.update()
    #titleScreen opener will go here
    def classPicker(i,num):
        if i==1:
            return Villain(num)
        elif i==2:
            return Burglar(num)
        elif i==3:
            return AntivirusProgrammer(num)
        elif i==4:
            return Doctor(num)
        elif i==5:
            return Hacker(num)
        elif i==6:
            return Police(num)
        elif i==7:
            return Librarian(num)

    def quit(window):
        window.close()
        pygame.display.quit()
        sys.exit

    def isWithin(point,foX1,foY1,foX2,foY2,aa): #For ovals
        pX1 = (point[0]-foX1)**2
        pX2 = (point[0]-foX2)**2
        pY1 = (point[1]-foY1)**2
        pY2 = (point[1]-foY2)**2
        return aa >= ((pX1+pY1)**.5 + (pX2+pY2)**.5)
    
    while atTitleScreen:   # Title Screen event Loop here
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                quit(game_screen)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,482,199,680,199,240):#Foci coordinates and 2a value of Start button
                    atTitleScreen = False
                if isWithin(click,350,660,800,660,485):#Foci xy's and 2a of Exit button
                    quit(game_screen)
    atStartPage = True

    mainScreens.displayStartPage(game_screen)
    pygame.display.update()
    isHost = False
    while atStartPage:   # Host/Join Game screen event Loop here
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                quit(game_screen)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,456,337,296,337,240):#Host Game
                    connectionType = Server()
                    isHost = True
                    atStartPage = False
                if isWithin(click,904,337,744,337,240):#Join Game
                    connectionType = Client()
                    atStartPage = False
                if isWithin(click,821,668,371,668,484):#Exit
                    quit(game_screen)

    isConnecting = True
    minPlayerCount = 1

    def leave(window):
        if not isHost:
            connectionType.sendStrToServer('quit')
        else:
            connectionType.endGame()
        quit(window)

    def loadingScreen(window):
        isLoading = True
        rUp = True
        gUp = True
        bUp = True
        x = time.clock()+.01
        while isLoading:
            while x < time.clock():
                x = time.clock()+.01
                if rUp:
                    r += random.randint(0,1)
                    if r > 255:
                        rUp = False
                else:
                    r -= random.randint(0,1)
                    if r < 0:
                        rUp = True
                if gUp:
                    g += random.randint(0,1)
                    if g > 255:
                        gUp = False
                else:
                    g -= random.randint(0,1)
                    if g < 0:
                        gUp = True
                if bUp:
                    b += random.randint(0,1)
                    if b > 255:
                        bUp = False
                else:
                    b -= random.randint(0,1)
                    if b < 0:
                        bUp = True
                window.fill(r,g,b)

    while isConnecting:  # Host/Client connecting screen event loop here
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                leave(game_screen)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isHost:
                    if connectionType.getPlayerCount() >= minPlayerCount and isWithin(click,950,167,686,167,320):#Start Game
                        isConnecting = False
                    if isWithin(click,950,400,686,400,320): #Alternate Broadcasting type
                        connectionType.backupBroadCast()
                if isWithin(click,950,633,686,633,320):#Exit
                    leave(game_screen)
        mainScreens.displayConnectionPage(game_screen)
        if not isHost: #draw screen
            if connectionType.getStr() == 'start':  # All client programs start game
                isConnecting = False
            pygame.draw.rect(game_screen, blue, (630,60,370,450))
            if connectionType.getInt() > 1:
                for i in range(connectionType.getInt()):
                    pygame.draw.rect(game_screen,green,(64,131+50*i,319,34))
        if isHost: #draw screen
            if connectionType.getPlayerCount() < minPlayerCount:
                pygame.draw.rect(game_screen,blue,(630,60,370,210))
            if connectionType.getPlayerCount() > 1:
                for i in range(connectionType.getPlayerCount()):
                    connectionType.sendIntToPlayer(connectionType.getPlayerCount(),i)
                    pygame.draw.rect(game_screen,green,(64,131+50*i,319,34))
        pygame.display.update()
    #done
    loading = threading.Thread(target = loadingScreen, args = (game_screen), daemon = True)
    loading.start()
    if isHost: #Notifys players to start game and adds variable for the total number of players
        connectionType.startGame()
        numPlayers = connectionType.getPlayerCount()
    else:
        numPlayers = connectionType.getInt()
    time.sleep(1)
    if isHost: # provides playerNumbers to every player, self included
        classList = [1]
        myNum = 1
        for i in range(numPlayers):
            classList.append(random.randint(2, numberOfClasses))
        random.shuffle(classList)
        for i in range(numPlayers-1):
            connectionType.sendIntToPlayer(i+2, i)
    else:
        myNum = connectionType.getInt()
    time.sleep(1)
    if isHost: # provides character class roles to every player
        myClassNum = classList[0]
        for i in range(numPlayers-1):
            connectionType.sendIntToPlayer(classList[i+1],i)
    else:
        myClassNum = connectionType.getInt()
    isLoading = False
    myClass = classPicker(myClassNum, myNum)
    
    a = CharacterScreen(game_screen,myClass) # Shows character role and info regarding it
    time.sleep(TIME_THAT_WE_SHOULD_HAVE_THEM_READ_THEIR_CHARACTER_INFO_FOR)

    #What next, board? gameplay?

    print('done!!!')