import Character
import pygame, random, time

class McAgeeCustomerSupport(Character.Character):


    self.className = 'AntiVirus Customer Support'
    self.goal = 'get rid of the nagging customer'
    self.abilityDefinition = 'Figure out to type "Hello, World" with a mixed-up keyboard'
    self.minigameName = '"HelloWorld"'
    self.abilSuccess = 'You successfully provided minimal assistance to your helpless customer'
    self.abilLoss = 'You fail to defeat the notorious hacker'
    self.gamePoints = 0
    self.playerNumber = -1

    def minigame(self):
        response = ''
        isUprCase = False

        minigameWon = False
        minigameLost = False
        while not minigameWon and not minigameLost:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    return
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        xPos += spaceBetweenLetters
                    if event.key == K_RIGHT:
                        xPos -= spaceBetweenLetters
                    if event.key == K_1:
                        isCircle = False
                    if event.key == K_2:
                        isCircle = True
                window.fill((0,0,0))