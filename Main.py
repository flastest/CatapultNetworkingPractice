# this is the main function for the game
# dimensions of the game will be 1200x800


import pygame 
from pygame.locals import *
from Burglar import *

class Main(object):
    #titleScreen opener will go here
    print('test')
    test = Burglar(88)
    
    print("Class =",test)
    print("minigame loss results in:",test.getMinigameLossText())

    print("image name is:",test.getAvatar())    

    screen = pygame.display.set_mode([1200,800])
    pygame.display.set_caption("My Window")
    test.drawCharacter(100,100,screen)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()

