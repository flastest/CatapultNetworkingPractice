import pygame, time
from pygame.locals import *

class OperationMinigame():

    You_Win = False
    def __init__(self,screen):
        self.minigame(screen)
    def minigame(self, screen):
        startTime = time.clock()
        pygame.init()
        screen = pygame.display.set_mode([1200,800])
        background = pygame.image.load('Background for Operation game.png')
        youWin = pygame.image.load('You Win.png')
        lungs = pygame.image.load('lungs.png')
        lungs = pygame.transform.scale(lungs,(300,300))
        brain = pygame.image.load('Brain.png')
        brain = pygame.transform.scale(brain,(150,150))
        liver =pygame.image.load('Liver.png')
        liver = pygame.transform.scale(liver,(170,170))
        largeIntestine = pygame.image.load('LargeIntestine.png')
        largeIntestine = pygame.transform.scale(largeIntestine,(300,300))
        heart = pygame.image.load('Heart.png')
        stomach = pygame.image.load('Stomach.png')
        stomach = pygame.transform.scale(stomach, (150,150))
        Bodylist = [heart,brain,stomach,liver,largeIntestine,lungs]
        # global lung_remove
        lung_remove = False
        heart_remove = False
        liver_remove = False
        stomach_remove = False
        largeIntestine_remove = False
        brain_remove = False


        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    P = pygame.mouse.get_pos()
                    #removes lung
                    if P[0] <= 300+300 and P[0] >= 300 and P[1] <= 200+300 and P[1] >= 200:
                        if P[0] <= 410+100 and P[0] >= 410 and P[1] <= 300+100 and P[1] >= 300:
                            pass
                        else:
                            lung_remove = True
                    #removes heart
                    if P[0] <= 410+100 and P[0] >= 410 and P[1] <= 300+100 and P[1] >= 300:
                        if lung_remove == True:
                            heart_remove = True
                    #removes stomach
                    if P[0] <= 430+150 and P[0] >= 430 and P[1] <= 390+150 and P[1] >= 390:
                        if P[0] <= 340+170 and P[0] >= 340 and P[1] <= 390+170 and P[1] >= 390:
                            pass
                        elif P[0] <= 300+300 and P[0] >= 300 and P[1] <= 450+300 and P[1] >= 450:
                            pass
                        else:
                            if heart_remove == True:
                                stomach_remove = True
                            else:
                                lung_remove = False
                    #removes liver
                    if P[0] <= 340+170 and P[0] >= 340 and P[1] <= 390+170 and P[1] >= 390:
                        if P[0] <= 300+300 and P[0] >= 300 and P[1] <= 450+300 and P[1] >= 450:
                            pass
                        else:
                            if stomach_remove == True:
                                liver_remove = True
                            else:
                                lung_remove = False
                                heart_remove = False
                    #removes largeIntestine
                    if P[0] <= 300+300 and P[0] >= 300 and P[1] <= 450+300 and P[1] >= 450:
                        if liver_remove == True:
                            largeIntestine_remove = True
                        else:
                            lung_remove = False
                            heart_remove = False
                            stomach_remove = False
                    #removes brain
                    if P[0] <= 400+150 and P[0] >= 400 and P[1] <= 0+150 and P[1] >= 0:
                        if largeIntestine_remove == True:
                            brain_remove = True
                            self.You_Win = True

                        else:
                            lung_remove = False
                            heart_remove = False
                            stomach_remove = False
                            liver_remove = False
            
            newfont = pygame.font.Font(None, 300)
            loseText = newfont.render("You Lose",0,(255,0,0))
            timeLeft = int(10 - (time.clock()-startTime))
            screen.fill((0,0,0))
            screen.blit(background, (0,0))
            if timeLeft <= 0 and self.You_Win == False:
                screen.blit(loseText, (100,100))
                pygame.display.update()
                pygame.time.wait(2000)
                running = False
            font =  pygame.font.Font(None, 50)
            text = font.render("Timer: "+str(timeLeft),0,(0,0,0))
            screen.blit(text,(0,0))
            for x in Bodylist:
                if x == lungs and lung_remove == False:
                    screen.blit(lungs,(300,200))
                elif x == heart and heart_remove == False:
                    screen.blit(heart,(410,300))
                elif x == liver and liver_remove == False:
                    screen.blit(liver,(340,390))
                elif x == stomach and stomach_remove == False:
                    screen.blit(stomach,(430,390))
                elif x == largeIntestine and largeIntestine_remove == False:
                    screen.blit(largeIntestine,(300,450))
                elif x == brain and brain_remove == False:
                    screen.blit(brain, (400, 0))
            if self.You_Win == True:
                screen.blit(youWin,(0,0))
                pygame.display.update()
                time.sleep(2)
                running  = False
            pygame.display.update()
#s = pygame.display.set_mode([1,1])
#a = OperationMinigame(s)