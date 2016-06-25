import pygame
from pygame.locals import *

class TitleScreen:
    def __init__(self):
        self.image = pygame.image.load('TitleScreen.png')
        
    def display(self,window):
        window = pygame.display.set_mode([0,0])
        window.blit(self.image,(0,0))
    
