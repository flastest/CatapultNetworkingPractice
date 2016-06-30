import pygame
from pygame import *
from Burglar import *
class CharacterScreen:

    def __init__ (self, window, Character):
        isRunning = True
        window = pygame.display.set_mode([800,500])
        Name = Character.getName()
        Goal = 'Your goal is to ' + Character.getGoal()
        black = (0,0,0)
        gray = (30,30,30)
        lBrown = (222,184,135)
        
        window.fill(lBrown)

        font = pygame.font.Font(None, 40)
        nameFont = pygame.font.Font('times.ttf', 72)
        goalFont = pygame.font.Font(None, 24)

        text = font.render('Your Role is:', 1, gray)
        textW,textH = font.size('Your Role is:')
        window.blit(text, (400-textW/2,100))

        text2 = nameFont.render(Name,1,black)
        textW,textH = nameFont.size(Name)
        window.blit(text2, (400-textW/2,180))

        text3 = goalFont.render(Goal,1,black)
        textW,textH = goalFont.size(Goal)
        window.blit(text3, (400-textW/2,350))

        pygame.display.update()