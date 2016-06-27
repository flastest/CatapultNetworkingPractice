import pygame
from pygame.locals import *

class TitleScreen:

    titleScreenImage = 'TitleScreen2.png'
    startPageImage = 'StartPage.png'
    connectionPageImage = 'ConnectingPage.png'
        
    def displayTitleScreen(self,window):
        pygame.init()
        window = pygame.display.set_mode([0,0])
        window.blit(pygame.image.load(self.titleScreenImage),(0,0))
    
    def displayStartPage(self,window):
        pygame.init()
        window = pygame.display.set_mode([0,0])
        window.blit(pygame.image.load(self.startPageImage),(0,0))

    def displayConnectionPage(self,window):
        pygame.init()
        window = pygame.display.set_mode([0,0])
        window.blit(pygame.image.load(self.connectionPageImage),(0,0))