import pygame
from pygame.locals import *

class TitleScreen:
    def __init__(self, window,x,y):
        image = pygame.image.load('TitleScreen.png')
        window = pygame.display.set_mode([x,y])
        x=1500
        y=1500
    