import Character
import pygame, random, time
from pygame.locals import *

class Hacker(Character.Character):


    className = 'Hacker'
    goal = 'hack into the interwebs and steal digital information.'
    abilityDefinition = 'break through the opposing firewall.'
    minigameName = '1337 hax'
    abilSuccess = 'You successfully hack your target.'
    abilLoss = 'You fail to hack your target.'
    gamePoints = 0
    playerNumber = -1
    timeLimit = 50 # time limit for the minigame, feel free to change as needed.
    image = 'Hacker.png'
    
    def display(self,window,coordinates):
        window.blit(pygame.image.load(self.image),(coordinates[0],coordinates[1]))
        
    def minigame(self, window, t):
        minigameWon = False
        minigameLost = False
        startTime = time.clock()

        pygame.init()
        window = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Firewall fight')

        white = [255,255,255]
        gray = [130,130,130]
        black = [0,0,0]
        rd = [255,0,0]
        red = [255, 100, 0]
        green = [0,255,0]
        blue = [0,0,255]
        wall = [600,200]
        fwW = 300
        fwH = 150
        dFw = []
        fwAtt = []
        player = [600, 615]
        attackTime = 0
        fwDMove = 0
        fwMoveTime = 0
        fwTime = time.clock() + 1
        fwAttTime = time.clock() + 1
        fwGval = 100
        fwGval = 0
        attacks = []
        attTi = time.clock() + .02
        lines = []
        nextTime = False
        for i in range(16):
            lines.append([0,0,0,0,255,0,0])
        hp = 24
        tP = 0
        ended = False
        lIsPressed = False
        rIsPressed = False
        spHeld = False
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
                    if event.key == K_SPACE:
                        spHeld = False
                    tP = 0
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        lIsPressed = True
                    if event.key == K_RIGHT:
                        rIsPressed = True
                    if event.key == K_SPACE:
                        spHeld = True
                        if attackTime < time.clock():
                            attacks.append((player[0], player[1]-25))
                            attackTime = time.clock() + .7
                    tP = time.clock()
            if spHeld:
                if attackTime < time.clock():
                    attackTime = time.clock()+.7
                    attacks.append((player[0],player[1]-20))
            if tP < time.clock():
                tP = time.clock()+.05
                if rIsPressed:
                    player[0] += 5
                if lIsPressed:
                    player[0] -= 5
            if fwDMove < time.clock():
                fwDMove = time.clock() + 8
                xVal = 8
                yVal = 6
                minVal = 3
                if time.clock() > startTime + 35:
                    xVal = 12
                    yVal = 10
                    minVal = 6
                dx = random.randint(-xVal,xVal)
                dy = random.randint(-yVal,yVal)
                while abs(dx) < minVal:
                    dx = random.randint(-xVal,xVal)
                while abs(dy) < minVal:
                    dy = random.randint(-yVal,yVal)
                dFw = [dx, dy]
            if fwMoveTime < time.clock():
                fwMoveTime = time.clock() + .03
                wall = [wall[0] + dFw[0], wall[1] + dFw[1]]
                if wall[0] <= fwW/2:
                    wall[0] = fwW/2
                    dFw[0] = -dFw[0]
                if wall[0] >= 1200-fwW/2:
                    wall[0] = 1200-fwW/2
                    dFw[0] = -dFw[0]
                if wall[1] >= 400-fwH/2:
                    wall[1] = 400-fwH/2
                    dFw[1] = -dFw[1]
                if wall[1] <= 60+fwH/2:
                    wall[1] = 60+fwH/2
                    dFw[1] = -dFw[1]
                if nextTime:
                    lines[i][0] = lines[i][0] + dFw[0]
                    lines[i][1] = lines[i][1] + dFw[1]
                    lines[i][2] = lines[i][2] + dFw[0]
                    lines[i][3] = lines[i][3] + dFw[1]
                    nextTime = not nextTime
                else:
                    for i in range(len(lines)):
                        fwGval = random.randint(20,120)
                        fwBval = random.randint(0,20)
                        lines[i][0] = random.randint(wall[0]-10-fwW/2, wall[0]+10+fwW/2)
                        lines[i][1] = random.randint(wall[1]-10-fwH/2, wall[1]+10+fwH/2)
                        lines[i][2] = random.randint(wall[0]-10-fwW/2, wall[0]+10+fwW/2)
                        lines[i][3] = random.randint(wall[1]-10-fwH/2, wall[1]+10+fwH/2)
                        lines[i][5] = random.randint(0,100)
                        lines[i][6] = random.randint(0,30)
                    nextTime = not nextTime
            if fwTime < time.clock(): #spawn rate of fireballs
                x = .5
                if time.clock() > startTime + 20:
                    x = .4
                if time.clock() > startTime + 35:
                    x = .3
                fwTime = time.clock()+x
                spawnY = wall[1]+(fwH/2) + 5
                attDX = (player[0]-wall[0])//random.randint(64,72)
                attDY = (player[1]-spawnY)//random.randint(64,72)
                fwAtt.append([wall[0], spawnY, int(attDX), int(attDY)])
            if player[0] <= 5:
                player[0] = 5
            if player[0] >= 1195:
                player[0] = 1195
            window.fill(black)
            if fwAttTime < time.clock():#move speed of fireballs
                x = .04
                if time.clock() > startTime + 20:
                    x = .03
                if time.clock() > startTime + 35:
                    x = .02
                fwAttTime = time.clock() + x
                for i in range(len(fwAtt)):
                    if fwAtt[i][1] > 800:
                        del fwAtt[i]
                        break
                for i in range(len(fwAtt)):
                    fwAtt[i][0] = fwAtt[i][0]+fwAtt[i][2]
                    fwAtt[i][1] = fwAtt[i][1]+fwAtt[i][3]
                    if fwAtt[i][0] >= player[0]-8 and fwAtt[i][0] <= player[0]+8 and fwAtt[i][1] >= player[1]-10 and fwAtt[i][1] <= player[1]+10:
                        minigameLost = True
            if time.clock() > attTi:
                attTi = time.clock() + .03
                for i in range(len(attacks)):
                    if attacks[i][1] < 60:
                        del attacks[i]
                        break
                for i in range(len(attacks)):
                    attacks[i] = (attacks[i][0], attacks[i][1]-5)
                    if attacks[i][1] <= wall[1]+fwH/2 and attacks[i][1] >= wall[1]-fwH and attacks[i][0] >= wall[0]-fwW/2 and attacks[i][0] <= wall[0]+fwW/2:
                        hp -= 1
                        del attacks[i]
                        break
            for i in range(len(attacks)):
                pygame.draw.circle(window, blue, attacks[i], 5)
            for i in range(len(fwAtt)):
                pygame.draw.circle(window, rd, (int(fwAtt[i][0]), int(fwAtt[i][1])), 3)
                pygame.draw.line(window, rd, (fwAtt[i][0],fwAtt[i][1]), (fwAtt[i][0]-2*fwAtt[i][2], fwAtt[i][1]-3*fwAtt[i][3]), 3)
            pygame.draw.rect(window, rd, (0,0,1200,60))
            pygame.draw.rect(window, green, (0,0, hp*(1200/24),60))
            pygame.draw.polygon(window,white,((player[0],player[1]-15),(player[0]-10, player[1]+10), (player[0]+10,player[1]+10)),0)
            pygame.draw.rect(window, (255, fwGval, fwBval), (wall[0]-fwW/2, wall[1]-fwH/2, fwW, fwH))
            for i in range(len(lines)):
                pygame.draw.line(window, (lines[i][4],lines[i][5],lines[i][6]), (lines[i][0],lines[i][1]), (lines[i][2],lines[i][3]), random.randint(1,5))
            font = pygame.font.Font(None, 28)
            text = font.render(str(int(self.timeLimit+startTime-time.clock())), 1, black)
            txt = font.render('Use the arrowkeys to move and the spacebar to fire.', 1, black)
            window.blit(txt, (8,8))
            window.blit(text, (1165,8))
            pygame.display.update()
            if hp == 0:
                minigameWon = True
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
            window.fill([0,0,0])
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
            window.fill((0,0,0))
            font = pygame.font.Font(None, 36)
            text = font.render(words, 1, (255,255,255))
            countdown = font.render('Returning to the main game in:     ' + str(t-i) , 1, (255,255,255))
            window.blit(text, (8,8))
            window.blit(countdown, (8, 100))
            pygame.display.update()
            time.sleep(1)
#a = Hacker(1)
#a.showRules()