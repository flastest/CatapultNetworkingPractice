import Character
import pygame, time, random
from pygame.locals import *

class Villain(Character.Character):
    className = 'Villain'
    goal = 'avoid being discovered as the villain and prevent their success.'
    abilityDefinition = 'sabotage the other player by destroying the objectives in order.'
    minigameName = 'Sabotage'
    abilSuccess = 'You successfully sabotage the player.'
    abilLoss = 'You fail to sabotage the player.'
    timeLimit = 50 # minigame time limit, feel free to change as needed
    image = 'Villain.png'
    
    def display(self,window,coordinates):
        window.blit(pygame.image.load(self.image),(coordinates[0],coordinates[1]))

    def minigame(self, window, t):
        minigameWon = False
        minigameLost = False
        startTime = time.clock()
        
        pygame.init()
        pygame.display.set_caption('Breaking things. . .')
        white = [255,255,255]
        gray = [100,100,100]
        red = [120,30,30]
        black = [0,0,0]

        player = [590,390]
        obj = []
        objDst = []
        nope = True
        for i in range(16):
            objDst.append(False)
            obj.append((random.randint(8,1172), random.randint(38,672)))
            while nope:
                nope = False
                if (obj[i][0] >= 390 and obj[i][0] <= 790 and obj[i][1] >= 190 and obj[i][1] <= 590):
                    nope = True
                for j in range(len(obj)):
                    if j < i:
                        if abs(obj[i][0] - obj[j][0]) < 12 or abs(obj[i][1] - obj[j][1]) < 12:
                            nope = True
                if nope:
                    obj[i] = (random.randint(8,1172), random.randint(38,672))
        attackTime = 0
        tP = 0
        ended = False
        lIsPressed = False
        rIsPressed = False
        uIsPressed = False
        dIsPressed = False
        while not minigameWon and not minigameLost:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    ended = True
                    break
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        lIsPressed = False
                    if event.key == K_RIGHT:
                        rIsPressed = False
                    if event.key == K_UP:
                        uIsPressed = False
                    if event.key == K_DOWN:
                        dIsPressed = False
                    tP = 0
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        lIsPressed = True
                    if event.key == K_RIGHT:
                        rIsPressed = True
                    if event.key == K_UP:
                        uIsPressed = True
                    if event.key == K_DOWN:
                        dIsPressed = True
                    if event.key == K_SPACE:
                        attackTime = time.clock() + .05
                    tP = time.clock()
            if tP < time.clock():
                tP = time.clock()+.001
                if uIsPressed:
                    player[1] -= 4
                if dIsPressed:
                    player[1] += 4
                if rIsPressed:
                    player[0] += 4
                if lIsPressed:
                    player[0] -= 4
            if player[0] < 0:
                player[0] = 1180
            if player[0] > 1180:
                player[0] = 0
            if player[1] < 30:
                player[1] = 770
            if player[1] > 770:
                player[1] = 30
            window.fill(gray)
            pygame.draw.rect(window, white, (0,0,1200,30))
            pygame.draw.rect(window, (50,255,50), (player[0], player[1], 20, 20))
            font = pygame.font.Font(None, 28)
            text = font.render(str(int(self.timeLimit+startTime-time.clock())), 1, black)
            txt = font.render('Use the arrowkeys to move and the spacebar to destroy objectives.', 1, black)
            window.blit(txt, (8,8))
            window.blit(text, (1165,8))
            count = 0
            for i in range(16):
                if objDst[i]:
                    if count < i:
                        minigameLost = True
                    count += 1
                if not objDst[i]:
                    pygame.draw.circle(window, red, (obj[i][0],obj[i][1]), 13)
                    ft = pygame.font.Font(None,18).render(str(i+1),1,white)
                    window.blit(ft,(obj[i][0]-7,obj[i][1]-5))
                if attackTime > time.clock() and (abs(player[0]+10-obj[i][0])**2 + abs(player[1]+10-obj[i][1])**2)**.5 <= 30:
                    objDst[i] = True
            if count == 16:
                minigameWon = True
            pygame.display.update()
            if time.clock()-startTime >= self.timeLimit:
                minigameLost = True
            if ended:
                pygame.display.quit()
                break
        if minigameWon or minigameLost:
            self.showEndScreen(window, minigameWon, t)

    def showRules(self, t = 5):
        pygame.init()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill([100,100,100])
            font = pygame.font.Font(None, 36)
            goal = 'Your objective is to ' + self.getAbilityDefinition()
            text1 = font.render(goal, 1, (255,255,255))
            countdown = font.render('Minigame starting in:     ' + str(t-i) , 1, (255,255,255))
            window.blit(text1, (8,8))
            window.blit(countdown, (8, 100))
            pygame.display.update()
            time.sleep(1)
        self.minigame(window, t)

    def showEndScreen(self, window, hasWon, t):
        if hasWon:
            words = self.getMinigameWinText()
            self.getPoints(1)
        else:
            words = self.getMinigameLossText()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill((100,100,100))
            font = pygame.font.Font(None, 36)
            text = font.render(words, 1, (255,255,255))
            countdown = font.render('Returning to the main game in:     ' + str(t-i) , 1, (255,255,255))
            window.blit(text, (8,8))
            window.blit(countdown, (8, 100))
            pygame.display.update()
            time.sleep(1)

#a = Villain(1)
#a.showRules(5)