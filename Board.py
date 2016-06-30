import pygame
from pygame.locals import *

#Settings for board
class Board:

    WHITE = [255,255,255]
    GREEN = [0,255, 0]
    PATH_SELECTION_YELLOW = (255,220,55)
    BLACK = [0,0,0]
    BROWN = [139,69,19]
    LIGHTBROWN = [222,184,135]
    hasNotWon = True
    xCoord = (0,0)
    xCoord2 = (0,800)
    yCoord = (0,0)
    yCoord2 = (1200,0)
    size = (1200, 800)
    moveCount = 0
    initSpaces = 0
    moveValues = []
    initPos = [0,0]
    myPos = [0,0]
    goalCoordinates = [11,7]
    isTurn = True
    points = 0

    def __init__(self,screen):
        self.win = screen

    def setBoard(self):
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption('GAMEBOARD - COOKIE SCAM ')
        self.win.fill(self.BROWN)
        for x in range(13):
            pygame.draw.line(self.win, self.LIGHTBROWN, (self.xCoord[0]+75*x,0), (self.xCoord2[0]+75*x,600), 3)
        for y in range(9):
            pygame.draw.line(self.win, self.LIGHTBROWN, (0,self.yCoord[1] +75 * y), (900, self.yCoord2[1] +75 *y), 3)
    
    def showCharacter(self, img, mapCoordinates = myPos):
        self.win.blit(img, (mapCoordinates[0]*75,mapCoordinates[1]*75))

    def goThere(self,img):
        if self.moveCount < self.initSpaces:
            self.moveValues[:] = []
            self.moveSpaces = 0
            self.isTurn = False
    def isntRepeated(self, pos):
        isOk = True
        for i in range(len(self.moveValues)):
            if (pos[0],pos[1]) == (self.moveValues[i][0],self.moveValues[i][1]) or (pos[0],pos[1]) == (self.initPos[0],self.initPos[1]):
                print('nope')
                isOk = False
        return isOk
    def left(self):
        if self.myPos[0] > 0 and self.moveCount > 0 and self.isntRepeated((self.myPos[0]-1,self.myPos[1])):
            self.moveValues.append([self.myPos[0]-1,self.myPos[1]])
            self.moveCount -= 1
            self.myPos = [self.myPos[0]-1,self.myPos[1]]
    def right(self):
        if self.myPos[0] < 11 and self.moveCount and self.isntRepeated((self.myPos[0]+1,self.myPos[1])):
            self.moveValues.append([self.myPos[0]+1,self.myPos[1]])
            self.moveCount -= 1
            self.myPos = [self.myPos[0]+1,self.myPos[1]]
    def up(self):
        if self.myPos[1] > 0 and self.moveCount > 0 and self.isntRepeated((self.myPos[0],self.myPos[1]-1)):
            self.moveValues.append([self.myPos[0],self.myPos[1]-1])
            self.moveCount -= 1
            self.myPos = [self.myPos[0],self.myPos[1]-1]
    def down(self):
        if self.myPos[1] < 7 and self.moveCount > 0 and self.isntRepeated((self.myPos[0],self.myPos[1]+1)):
            self.moveValues.append([self.myPos[0],self.myPos[1]+1])
            self.moveCount -= 1
            self.myPos = [self.myPos[0],self.myPos[1]+1]
    def restartPath(self):
        self.myPos = self.initPos
        self.moveCount = self.initSpaces
        self.moveValues[:] = []
        self.moveValues = []
    def turnStart(self,moveSpaces):
        self.initPos = self.myPos
        self.initSpaces = moveSpaces
        self.moveCount = moveSpaces
        self.isTurn = True
    def displayUnconfirmedPath(self):
        if len(self.moveValues) > 0:
            for i in range(len(self.moveValues)):
                pygame.draw.rect(self.win,self.PATH_SELECTION_YELLOW,(self.moveValues[i][0]*75+2,self.moveValues[i][1]*75+2,72,72))
    def displayGoal(self):
        pygame.draw.circle(self.win,self.GREEN,(self.goalCoordinates[0]*75+37,self.goalCoordinates[1]*75+37),25)
        pygame.draw.circle(self.win,self.GREEN,(self.goalCoordinates[0]*75+37,self.goalCoordinates[1]*75+38),25)
        pygame.draw.circle(self.win,self.GREEN,(self.goalCoordinates[0]*75+38,self.goalCoordinates[1]*75+37),25)
        pygame.draw.circle(self.win,self.GREEN,(self.goalCoordinates[0]*75+38,self.goalCoordinates[1]*75+38),25)
    def moveGoal(self):
        self.points += 1
        if self.points == 1:
            self.goalCoordinates[:] = [0,7]
        elif self.points == 2:
            self.goalCoordinates[:] = [11,0]
        elif self.points == 3:
            self.goalCoordinates[:] = [0,0]
        else:
            self.goalCoordinates[:] = [-5,-5]
            self.isTurn = False
            self.hasNotWon = False
