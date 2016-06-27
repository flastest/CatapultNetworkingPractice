# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame 
from pygame.locals import *
from Burglar import *
from TitleScreen import *

class Main:
    atTitleScreen = True
    closed = False

    green = [34,177,76]
    blue = [63,72,204]
    pygame.init()
    mainScreens = TitleScreen()
    game_screen = pygame.display.set_mode([1200,800])
    pygame.display.set_caption("Cookie Scam")
    mainScreens.displayTitleScreen(game_screen)
    pygame.display.update()
    #titleScreen opener will go here
    
    #print('test')
    #test = Burglar(88)
    #print("Class =",test)
    #print("minigame loss results in:",test.getMinigameLossText())
    #print("image name is:",test.getAvatar())    
    #test.drawCharacter(100,100,game_screen)
    def quit(window):
        window.close()
        pygame.display.quit()
        sys.exit

    def isWithin(point,foX1,foY1,foX2,foY2,aa):
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
    while atStartPage:   # Host/Join Game screen event Loop here
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                quit(game_screen)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,456,337,296,337,240):#Join Game
                    connectionType = Server()
                    isHost = True
                    atStartPage = False
                if isWithin(click,904,337,744,337,240):#Host Game
                    connectionType = Client()
                    isHost = False
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

    while isConnecting:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                leave(game_screen)
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isHost:
                    if connectionType.getPlayerCount() >= minPlayerCount and isWithin(click,,,,,):#Start Game
                        #TODO
                        #START GAME!!!
                        isConnecting = False
                    if isWithin(click,,,,,): #Alternate Broadcasting type
                        connectionType.backupBroadCast()
                if isWithin(click,,,,,):#Exit
                    leave(game_screen)
        mainScreens.displayConnectionPage(game_screen)
        if not isHost:
            pygame.display.rect(game_screen, blue, ())
        pygame.display.update()
    print('done!!!')