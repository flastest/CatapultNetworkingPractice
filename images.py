import pygame, time
from pygame.locals import *

class images:
    img = pygame.image.load('Officer.png')


    def __init__(self):
        self.x,self.y = 0,0


    #screen = pygame.display.set_mode([800,800])
    #pygame.display.set_caption("My Window")

    def display(self,newX,newY,window):
        x = newX 
        y = newY

        window.blit(self.img,(x,y))
        pygame.display.flip()



        

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("My Window")
police = images()
police.display(100,100,screen)
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
        


