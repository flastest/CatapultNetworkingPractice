import pygame, sys
from pygame.locals import *
pygame.init()

#Settings for board
WHITE = [255,255,255]
GREEN = [0,255, 0]
BLACK = [0,0,0]
BROWN = [139,69,19]
LIGHTBROWN = [222,184,135]
xCoord = (0,0)
xCoord2 = (0,800)
yCoord = (0,0)
yCoord2 = (1200,0)
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('GAMEBOARD - COOKIE SCAM ')
screen.fill(BROWN)

while True:
    for x in range(13):
        pygame.draw.line(screen, LIGHTBROWN, (xCoord[0]+75*x,0), (xCoord2[0]+75*x,600), 3)
    for y in range(9):
        pygame.draw.line(screen, LIGHTBROWN, (0,yCoord[1] +75 * y), (900, yCoord2[1] +75 * y), 3 )
    events = pygame.event.get()
    pygame.display.update()
    for event in events:
        if event.type == QUIT:
            screen.close