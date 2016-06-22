import pygame, time
from pygame.locals import *

class images:
    

    def __init__(self,imageName):
        self.img = pygame.image.load(imageName)
        self.x,self.y = 0,0


    #screen = pygame.display.set_mode([800,800])
    #pygame.display.set_caption("My Window")

    def display(self,newX,newY,window):
        x = newX 
        y = newY

        window.blit(self.img,(x,y))
        pygame.display.flip()



        


# vv test vv
#screen = pygame.display.set_mode([800,800])
#pygame.display.set_caption("My Window")
#police = images("Officer.png")
#police.display(100,100,screen)
#while True:
#    events = pygame.event.get()
#    for event in events:
#        if event.type == QUIT:
#            pygame.quit()
        


