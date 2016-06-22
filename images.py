import pygame
from pygame.locals import *
img = pygame.image.load('Officer.png')

x,y, = 0,0

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("My Window")
running = 1

def putAt(newX,newY):
    x = newX 
    y = newY

    while running:
        
        screen.blit(img,(x,y))
        pygame.display.flip()


putAt(100,100)
