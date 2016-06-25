# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame 
from pygame.locals import *
from Burglar import *
from TitleScreen import *

class Main(object):
    game_screen = pygame.display.set_mode([1200,800])
    pygame.display.set_caption("Cookie Scam")
    #titleScreen opener will go here
    title = TitleScreen()
    title.display(game_screen)
    
    
    
    
    
    
    
    
    
    
    print('test')
    test = Burglar(88)
    
    print("Class =",test)
    print("minigame loss results in:",test.getMinigameLossText())

    print("image name is:",test.getAvatar())    

    test.drawCharacter(100,100,game_screen)
    
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()

