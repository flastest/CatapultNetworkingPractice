import Character
import pygame, time, random
from pygame.locals import *

class Burglar(Character.Character):

    className = 'Burglar'
    goal = 'steal as much as you can, while evading detection.'
    abilityDefinition = 'pick the lock that stands in your way.'
    minigameName = 'Lockpicking'
    abilSuccess = 'You successfully pick the lock.'
    abilLoss = 'You fail to pick the lock.'
    image = 'Robber.png'
    timeLimit = 60 # minigame time limit, feel free to change as needed

    def minigame(self, window, t):
        minigameWon = False
        minigameLost = False
        startTime = time.clock()
        
        pygame.init()
        pygame.display.set_caption('Picking lock . . .')
        lGray = [190,190,190]
        gray = [140,140,140]
        dGray = [100,100,100]
        white = [255,255,255]
        black = [0,0,0]
        pickX = 600
        pickY = 450
        pickW = 40
        pickH = 110
        dph = [0,0,0,0,0,0]
        pinSpot = [450,450,450,450,450,450]
        pin = []
        pinSprings = []
        pinW = 60
        pinH = 120
        pos = []
        for i in range(6):
            pin.append((385 + 60*i,pinSpot[i],pinW,pinH))
            pos.append(random.randint(370,440))
            pinSprings.append((90,90,90))

        ended = False
        canOpen = False
        uIsPressed = False
        dIsPressed = False
        rIsPressed = False
        lIsPressed = False
        tP = 0
        tH = [0,0,0,0,0,0]
        tHG = [0,0,0,0,0,0]
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
                    if event.key == K_RETURN:
                        if canOpen:
                            minigameWon = True
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        lIsPressed = True
                    if event.key == K_RIGHT:
                        rIsPressed = True
                    if event.key == K_UP:
                        uIsPressed = True
                    if event.key == K_DOWN:
                        dIsPressed = True
                    tP = time.clock()
            if tP < time.clock():
                tP = time.clock()+.06
                if uIsPressed:
                    pickY -= 5
                elif dIsPressed:
                    pickY += 5
                elif rIsPressed:
                    pickX += 5
                elif lIsPressed:
                    pickX -= 5
            window.fill(white)
            pygame.draw.rect(window, gray, [270, 180, 660, 440]) # topLeftX, topLeftY, width, height
            pygame.draw.rect(window, lGray, [380, 240, 480, 320])
            pygame.draw.rect(window, lGray, [270, 440, 120, 120])
            if pickY >= 450:
                pickY = 450
            if pickY <= 370:
                pickY = 370
            if pickX <= 380:
                pickX = 380
            if pickX >= 820:
                pickX = 820
            for i in range(6):
                if pickY < pinSpot[i]:
                    if pickX <= 450+80*i and pickX > 440+80*i and lIsPressed:
                        pickX = 450+80*i
                    if pickX >= 350+80*i and pickX < 360+80*i and rIsPressed:
                        pickX = 350+80*i
            for i in range(5):
                if pickX > 430+80*i and pickX < 450+80*i:
                    if pickY <= pinSpot[i]-5 and pickY <= pinSpot[i+1]-5:
                        pickY += 5
            for i in range(6):
                lVa = 0
                rVa = 0
                if i > 0:
                    if pickY >= pinSpot[i-1]:
                        lVa = 15
                if i < 5:
                    if pickY >= pinSpot[i+1]:
                        rVa = 15
                if pickX >= 370+80*i - lVa and pickX <= 430+80*i +rVa:
                    if pickY <= pinSpot[i]:
                        pinSpot[i] = pickY
                if pinSpot[i] < pickY or pickX <= 350+80*i or pickX >= 450+80*i:
                    if tH[i] < time.clock():
                        if tHG[i] > time.clock():
                            pinSpot[i] = pos[i]
                            dph[i] = 0
                        else:
                            tH[i] = time.clock()+.1
                            dph[i] += 1
                            pinSpot[i] += dph[i]
                            if pos[i] >= pinSpot[i] and pinSpot[i] >= pos[i] - 6:
                                dph[i] -= 5
                                if dph[i] <= 0:
                                    pinSpot[i] = pos[i]
                                    dph[i] = 0
                                    if tHG[i] < time.clock():
                                        tHG[i] = time.clock() + 20
                if pinSpot[i] >= 450:
                    pinSpot[i] = 450
                    dph[i] = 0
                pinSprings[i] = (pinSpot[i]-360, pinSpot[i]-360, pinSpot[i]-360)
                pygame.draw.rect(window, pinSprings[i], (400+80*i,240,40,120))
                pin[i] = ((390+80*i,pinSpot[i]-120,pinW,pinH))
                pygame.draw.rect(window, dGray, pin[i])
            font = pygame.font.Font(None, 28)
            txt = font.render('Use the arrowkeys to move, and press enter once the pins are in place to open the lock.', 1, black)
            window.blit(txt, (8,8))
            pygame.draw.rect(window, black, (pickX, pickY, pickW, pickH))
            pygame.draw.rect(window, black, (0, pickY+82, pickX, 28))
            pygame.display.update()
            count = 0
            for i in range(6):
                if pinSpot[i] == pos[i]:
                    count += 1
            if count == 6:
                canOpen = True
            else:
                canOpen = False
            if time.clock() > startTime + self.timeLimit:
                minigameLost = True
            if ended:
                pygame.display.quit()
                break
        if minigameWon or minigameLost:
            self.showEndScreen(window, minigameWon, t)

    def showRules(self, window, t = 5):
        pygame.init()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill((255,255,255))
            font = pygame.font.Font(None, 36)
            goal = 'Your objective is to ' + self.getAbilityDefinition()
            text1 = font.render(goal, 1, (0,0,0))
            countdown = font.render('Minigame starting in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text1, (8,8))
            window.blit(countdown, (8, 100))
            pygame.display.update()
            time.sleep(1)
        self.minigame(window, t)

    def showEndScreen(self, window, hasWon, t):
        self.won = hasWon
        if hasWon:
            words = self.getMinigameWinText()
        else:
            words = self.getMinigameLossText()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill((255,255,255))
            font = pygame.font.Font(None, 36)
            text = font.render(words, 1, (0,0,0))
            countdown = font.render('Returning to the main game in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text, (8,8))
            window.blit(countdown, (8, 100))
            pygame.display.update()
            time.sleep(1)
#b = pygame.display.set_mode([1,1])
#a = Burglar(1)
#a.showRules(b)