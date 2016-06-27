# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame 
from pygame.locals import *
from Burglar import *
from TitleScreen import *

class Main:
    atTitleScreen = True
    closed = False

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
                pygame.display.quit()
                break
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,482,199,680,199,240):#Foci coordinates and 2a value of Start button
                    atTitleScreen = False
                if isWithin(click,350,660,800,660,485):#Foci xy's and 2a of Exit button
                    pygame.display.quit()
                    break
    if closed:
        system.exit()
    atStartPage = True
    mainScreens.displayStartPage(game_screen)
    pygame.display.update()
    while atStartPage:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.display.quit()
                break
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                if isWithin(click,456,337,296,337,240):#Join Game
                    print('a')
                if isWithin(click,904,337,744,337,240):#Host Game
                    print('b')
                if isWithin(click,821,668,371,668,484):#Exit
                    pygame.display.quit()
                    break
    print('done!!!')