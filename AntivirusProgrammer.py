import Character
import pygame, random, time, os
from pygame.locals import *

class AntivirusProgrammer(Character.Character):


    className = 'an AntiVirus Programmer'
    goal = 'get rid of the nagging customer'
    abilityDefinition = 'Successfully type "Hello, World" with a mixed-up keyboard'
    minigameName = '"HelloWorld"'
    abilSuccess = 'You successfully provided minimal assistance to your helpless customer'
    abilLoss = 'You fail to defeat the notorious hacker'
    gamePoints = 0
    playerNumber = -1

    isUprCase = False # used in minigame function, do not use
    def insert(self, spot, word, letter): # used in mingame function, do not use
        if self.isUprCase:
            letter = letter.upper()
        word = word[:spot] + letter + word[spot:]
        spot += 1
        return word, spot

    def minigame(self):
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random.shuffle(letters)
        random.shuffle(letters)

        response = ''
        letterPosition = 0
        letterSize = 9

        minigameWon = False
        minigameLost = False
        startTime = time.clock()
        timeLimit = 100

        pygame.init()
        window = pygame.display.set_mode([400,200])
        shouldAppear = True
        pathName = os.path.abspath('McAgeeCustomerSupport.py')
        pathName = pathName[:len(pathName)-24] + '-Catapult-Networking-Practice\\times.ttf'
        x = time.clock()+.2
        while not minigameWon and not minigameLost:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    window.close()
                if event.type == KEYUP:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.isUprCase = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        response, letterPosition = self.insert(letterPosition, response, ' ')
                    if event.key == K_COMMA:
                        response, letterPosition = self.insert(letterPosition, response, ',')
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.isUprCase = True
                    if event.key == K_LEFT:
                        if letterPosition > 0:
                            letterPosition -= 1
                    if event.key == K_RIGHT:
                        if letterPosition < len(response):
                            letterPosition += 1 
                    if event.key == K_BACKSPACE:
                        if letterPosition > 0:
                            response = response[:letterPosition-1] + response[letterPosition:]
                            letterPosition -= 1
                    if event.key == K_DELETE:
                        if letterPosition < len(response)+1:
                            response = response[:letterPosition] + response[letterPosition+1:]
                    if event.key == K_a:
                        response, letterPosition = self.insert(letterPosition, response, letters[0])
                    if event.key == K_b:
                        response, letterPosition = self.insert(letterPosition, response, letters[1])
                    if event.key == K_c:
                        response, letterPosition = self.insert(letterPosition, response, letters[2])
                    if event.key == K_d:
                        response, letterPosition = self.insert(letterPosition, response, letters[3])
                    if event.key == K_e:
                        response, letterPosition = self.insert(letterPosition, response, letters[4])
                    if event.key == K_f:
                        response, letterPosition = self.insert(letterPosition, response, letters[5])
                    if event.key == K_g:
                        response, letterPosition = self.insert(letterPosition, response, letters[6])
                    if event.key == K_h:
                        response, letterPosition = self.insert(letterPosition, response, letters[7])
                    if event.key == K_i:
                        response, letterPosition = self.insert(letterPosition, response, letters[8])
                    if event.key == K_j:
                        response, letterPosition = self.insert(letterPosition, response, letters[9])
                    if event.key == K_k:
                        response, letterPosition = self.insert(letterPosition, response, letters[10])
                    if event.key == K_l:
                        response, letterPosition = self.insert(letterPosition, response, letters[11])
                    if event.key == K_m:
                        response, letterPosition = self.insert(letterPosition, response, letters[12])
                    if event.key == K_n:
                        response, letterPosition = self.insert(letterPosition, response, letters[13])
                    if event.key == K_o:
                        response, letterPosition = self.insert(letterPosition, response, letters[14])
                    if event.key == K_p:
                        response, letterPosition = self.insert(letterPosition, response, letters[15])
                    if event.key == K_q:
                        response, letterPosition = self.insert(letterPosition, response, letters[16])
                    if event.key == K_r:
                        response, letterPosition = self.insert(letterPosition, response, letters[17])
                    if event.key == K_s:
                        response, letterPosition = self.insert(letterPosition, response, letters[18])
                    if event.key == K_t:
                        response, letterPosition = self.insert(letterPosition, response, letters[19])
                    if event.key == K_u:
                        response, letterPosition = self.insert(letterPosition, response, letters[20])
                    if event.key == K_v:
                        response, letterPosition = self.insert(letterPosition, response, letters[21])
                    if event.key == K_w:
                        response, letterPosition = self.insert(letterPosition, response, letters[22])
                    if event.key == K_x:
                        response, letterPosition = self.insert(letterPosition, response, letters[23])
                    if event.key == K_y:
                        response, letterPosition = self.insert(letterPosition, response, letters[24])
                    if event.key == K_z:
                        response, letterPosition = self.insert(letterPosition, response, letters[25])
            window.fill((0,0,0))
            font = pygame.font.Font(pathName, 20)
            text = font.render(response, 1, (255,255,255))
            window.blit(text, (8,8))
            if shouldAppear:
                pygame.draw.line(window, (255,255,255), (letterSize*(letterPosition+1), 30), (2+letterSize*(letterPosition+2)-2, 30), 3)
            if time.clock() > x:
                shouldAppear = not shouldAppear
                x = time.clock() +.5
            pygame.display.update()
            if response == 'Hello, World':
                minigameWon = True
            if time.clock() > startTime + timeLimit:
                minigameLost = True