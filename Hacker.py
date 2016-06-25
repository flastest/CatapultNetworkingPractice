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

    def minigame(self, t):
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
        wall = []
        player = [600, 615]
        attackTime = 0
        attacks = []
        attTi = time.clock() + .02
        hp = 20
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
                            attackTime = time.clock() + .5
                    tP = time.clock()
            if spHeld:
                if attackTime < time.clock():
                    attackTime = time.clock()+.5
                    attacks.append((player[0],player[1]-20))
            if tP < time.clock():
                tP = time.clock()+.02
                if rIsPressed:
                    player[0] += 5
                if lIsPressed:
                    player[0] -= 5
            if player[0] <= 5:
                player[0] = 5
            if player[0] >= 1195:
                player[0] = 1195
            window.fill(black)
            if time.clock() > attTi:
                attTi = time.clock() + .02
                for i in range(len(attacks)):
                    if attacks[i][1] < 60:
                        del attacks[i]
                        break
                    attacks[i] = (attacks[i][0], attacks[i][1]-5)
            for i in range(len(attacks)):
                pygame.draw.circle(window, blue, attacks[i], 3)
            pygame.draw.rect(window, rd, (0,0,1200,60))
            pygame.draw.rect(window, green, (0,0, hp*60,60))
            pygame.draw.polygon(window,white,((player[0],player[1]-15),(player[0]-10, player[1]+10), (player[0]+10,player[1]+10)),0)
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
            pass#self.showEndScreen(window, minigameWon, t)
a = Hacker(1)
a.minigame(5)