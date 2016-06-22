import pygame, sys
from pygame.locals import *
from math import pi
pygame.init()

#Settings for board
WHITE = [255,255,255]
GREEN = [0,255, 0]
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('WELCOME TO THE GAME')
fps = 60
pygame.display.set_mode(size)
done = True
while done:
    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, (0, 0), (50,30), 1)
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            done = False
            

    



