# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame, random, threading, sys
from pygame.locals import *
from TitleScreen import *
from Server import *
from Client import *
from CharacterScreen import *
from Board import *

from AntivirusProgrammer import*
from Burglar import *
from Hacker import *
from Doctor import *
from Librarian import *
from Police import *
from Villain import *

class Main:
    numberOfClasses = 7    # CHANGE THIS AND classPicker() AS WE ADD MORE CHARACTER CLASSES
    TIME_THAT_WE_SHOULD_HAVE_THEM_READ_THEIR_CHARACTER_INFO_FOR = 5
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
    
    def classImgs(i):
        if i == 1:
            return 'Villain.png'
        if i == 2:
            return 'Robber.png'
        if i == 3:
            return 'Programmer.png'
        if i == 4:
            return 'doctor.png'
        if i == 5:
            return 'Hacker.png'
        if i == 6:
            return 'Officer.png'
        if i == 7:
            return 'Librarian.png'

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
                pygame.display.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,482,199,680,199,240):#Foci coordinates and 2a value of Start button
                    atTitleScreen = False
                if isWithin(click,350,660,800,660,485):#Foci xy's and 2a of Exit button
                    pygame.display.quit()
                    sys.exit()
    atStartPage = True

    mainScreens.displayStartPage(game_screen)
    pygame.display.update()
    isHost = False
    
    def leave(isHost,connectionType):
        if not isHost:
            connectionType.sendStrToServer('quit')
        else:
            connectionType.endGame()
        pygame.display.quit()
        sys.exit()
    
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
                    pygame.display.quit()
                    sys.exit()

    isConnecting = True
    minPlayerCount = 2
    if isHost:
        connectionType.initThreads()
    while isConnecting:  # Host/Client connecting screen event loop here
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                leave(isHost,connectionType)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,950,633,686,633,320):#Exit
                    leave(isHost,connectionType)
                if isHost:
                    if connectionType.numPlayers >= minPlayerCount and isWithin(click,950,167,686,167,320):#Start Game
                        isConnecting = False
                    if isWithin(click,950,400,686,400,320): #Alternate Broadcasting type
                        connectionType.backupBroadcast()
        mainScreens.displayConnectionPage(game_screen)
        if not isHost: #draw screen
            isConnecting = not connectionType.gameStarted
            connectionType.waitForStart()
            pygame.draw.rect(game_screen, blue, (630,60,370,450))
            if connectionType.rcvdInt >= 2:
                for i in range(connectionType.rcvdInt-1):
                    pygame.draw.rect(game_screen,green,(64,81+50*i,320,35))
        if isHost: #draw screen
            if connectionType.numPlayers < minPlayerCount:
                pygame.draw.rect(game_screen,blue,(630,60,370,210))
            if connectionType.numPlayers >= 2:
                for i in range(connectionType.numPlayers-1):
                    connectionType.sendStrToPlayer(str(connectionType.numPlayers),i)
                    pygame.draw.rect(game_screen,green,(64,81+50*i,320,35))
                time.sleep(.01)
        pygame.display.update()
    #done
    if isHost: #Notifys players to start game and adds variable for the total number of players
        connectionType.startGame()
        numPlayers = connectionType.numPlayers
        time.sleep(.01)
    else:
        numPlayers = connectionType.rcvdInt
    time.sleep(.5)
    if isHost: # provides playerNumbers to every player, self included
        classList = [1]
        myNum = 1
        for i in range(numPlayers-1):
            classList.append(random.randint(2, numberOfClasses))
        random.shuffle(classList)
        for i in range(numPlayers-1):
            connectionType.sendStrToPlayer(str(i+2), i)
    else:
        myNum = connectionType.rcvdInt
    time.sleep(.5)
    if isHost: # provides character class roles to every player
        myClassNum = classList[0]
        for i in range(numPlayers-1):
            connectionType.sendStrToPlayer(str(classList[i+1]),i)
    else:
        myClassNum = connectionType.rcvdInt
    isLoading = False
    myClass = classPicker(myClassNum, myNum)
    
    a = CharacterScreen(game_screen,myClass) # Shows character role and info regarding it
    time.sleep(TIME_THAT_WE_SHOULD_HAVE_THEM_READ_THEIR_CHARACTER_INFO_FOR-1)
    if not isHost:
        classList = []
    for i in range(numPlayers):
        if isHost:
            connectionType.sendStrToAll(str(classList[i]))
        else:
            classList.append(connectionType.rcvdInt)
        time.sleep(.1)

    #gameplay!!!!!!


    b = Board(game_screen)
    b.setBoard()
    myPic = pygame.transform.scale(pygame.image.load(myClass.getAvatar()),(75,75))
    picList = [myPic]
    coords = [b.initPos]
    beforeMyNum = True
    def showImgs(b,pics,xys):
        count = 0
        for i in range(len(pics)):
            show = True
            if count > 0:
                for j in range(count):
                    if xys[i] == xys[j]:
                        show = False
            if show:
                b.showCharacter(pics[i],xys[i])
            count += 1

    for i in range(numPlayers-1):
        if i+1 == myNum:
            beforeMyNum = False
        if beforeMyNum:
            picList.append(pygame.transform.scale(pygame.image.load(classImgs(i)),(75,75)))
        else:
            picList.append(pygame.transform.scale(pygame.image.load(classImgs(i+1)),(75,75)))
        coords.append((0,0))
    while b.hasNotWon:
        if not isHost:
            if connectionType.rcvdStr == 'lose':
                break
        else:
            for i in range(connectionType.numPlayers-1):
                if connectionType.rcvdStrs[i] == 'won':
                    break
        if not b.isTurn:
            if not isHost:
                if connectionType.rcvdStr == 'ok':
                    coords[0]=b.initPos
                    connectionType.sendStrToServer(str(b.initPos))
                    time.sleep(.01)
                    for i in range(numPlayers-1):
                        try:
                            tuple(connectionType.rcvdStr)
                            if i+1 != myNumber:
                                coords[i+1] = tuple(connectionType.rcvdStr)
                        except ValueError:
                            pass
                        time.sleep(.01)
                    connectionType.stopThread()
                    myClass.showRules(game_screen)
                    connectionType.resumeThread()
                    if not myClass.won:
                        b.setBoard()
                        showImgs(b,picList,coords)
                        b.displayGoal()
                        b.displayWaiting()
                        pygame.display.update()
                        time.sleep(3)
                else:
                    connectionType.sendStrToServer('ready')
            else:
                coords[0]=b.initPos
                tog = True
                for i in range(numPlayers-1):
                    if connectionType.rcvdStrs[i] != 'ready':
                        tog = False
                if tog:
                    for i in range(numPlayers-1):
                        connectionType.rcvdStrs[i] = 'not ready'
                    connectionType.sendStrToAll('ok')
                    time.sleep(.01)
                    for i in range(numPlayers-1):
                        coords[i+1] = connectionType.rcvdTuple[i]
                    time.sleep(.01)
                    for i in range(numPlayers):
                        connectionType.sendStrToAll(str(coords[i]))
                        time.sleep(.01)
                    connectionType.stopThread()
                    myClass.showRules(game_screen)
                    connectionType.resumeThread()
                    if not myClass.won:
                        b.setBoard()
                        showImgs(b,picList,coords)
                        b.displayGoal()
                        b.displayWaiting()
                        pygame.display.update()
                        time.sleep(3)
                else:
                    connectionType.sendStrToAll('wait')
            b.setBoard()
            showImgs(b,picList,coords)
            b.displayGoal()
            b.displayWaiting()
            pygame.display.update()
        if myClass.won:
            b.turnStart(myClass.speed)
            myClass.won = False
        while b.isTurn:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    leave(isHost,connectionType)
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        b.left()
                    if event.key == K_RIGHT:
                        b.right()
                    if event.key == K_DOWN:
                        b.down()
                    if event.key == K_UP:
                        b.up()
                    if event.key == K_ESCAPE:
                        b.restartPath()
                    if event.key == K_RETURN:
                        if not isHost:
                            connectionType.sendStrToServer('ready')
                        b.goThere(myPic)
            b.setBoard()
            showImgs(b,picList,coords)
            b.displayUnconfirmedPath()
            if (b.goalCoordinates[0],b.goalCoordinates[1]) == (b.initPos[0],b.initPos[1]):
                b.moveGoal()
            b.displayGoal()
            b.displayRules()
            pygame.display.update()
    notYet = True
    while notYet:
        game_screen.fill((255,255,255))
        if not isHost:
            connectionType.sendStrToServer('won')
            if not b.hasNotWon:
                pygame.image.load('You Win.png')
                notYet = False
            else:
                font = pygame.font.Font('times.ttf', 80)
                text = font.render('You Lose',1,(0,0,0))
                textW,textH = font.size('You Lose')
                self.game_screen.blit(text, (600-textW/2,400-textH/2))
                notYet = False
        if isHost:
            connectionType.sendStrToAll('lose')
            x = True
            for i in range(numPlayers-1):
                if connectionType.rcvdStrs[i] != 'won':
                    x = False
            if x:
                if b.hasNotWon:
                    font = pygame.font.Font('times.ttf', 80)
                    text = font.render('You Lose',1,(0,0,0))
                    textW,textH = font.size('You Lose')
                    self.game_screen.blit(text, (600-textW/2,400-textH/2))
                    notYet = False
                else:
                    pygame.image.load('You Win.png')
                    notYet = False
        pygame.display.update()
