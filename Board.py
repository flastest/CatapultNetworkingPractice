import pygame, sys
from pygame.locals import *
pygame.init()

#Settings for board
WHITE = [255,255,255]
GREEN = [0,255, 0]
BLACK = [0,0,0]
lines = 15
xCoord = (0,0)
xCoord2 = (0,300)

yCoord = (0,10)
yCoord2 = (400,10)


size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('WELCOME TO THE GAME')

screen.fill(BLACK)
for x in range(lines):
    xCoord[0] += 10
    xCoord2[0] += 10
    yCoord[1] -= 10
    yCoord2[1] -= 10
    pygame.draw.line(screen, GREEN, (xCoord[0],0), (xCoord2[0]+10,300), 3)
for y in range(lines):
    pygame.draw.line(screen, GREEN, (0,yCoord[1] -10), (400, yCoord2[1] - 10), 3 )
events = pygame.event.get()
pygame.display.update()
for event in events:
    if event.type == QUIT:
        screen.close


            
            

    



