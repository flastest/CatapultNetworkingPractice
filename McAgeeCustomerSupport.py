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
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't','u','v','w','x','y','z']
        random.shuffle(letters)
        random.shuffle(letters)

        response = ''
        letterPosition = 0
        letterSize = 20
        isUprCase = False

        minigameWon = False
        minigameLost = False
        startTime = time.clock()

        window = pygame.display.set_mode([400,200])
        pygame.display.set_caption('"cmd"')

        while not minigameWon and not minigameLost:
            x = time.clock()
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    window.close()
                if event.type == KEYUP:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        isUprCase = False
                if event.type == KEYDOWN:
                    if event.key == SPACE:
                        self.insert(letterPosition, response, ' ')
                        letterPosition += 1
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        isUprCase = True
                    if event.key == K_LEFT:
                        if letterPosition > 0:
                            letterPosition -= 1
                    if event.key == K_RIGHT:
                        if letterPosition < len(response):
                            letterPosition += 1 
                window.fill((255,255,255))
                pygame.draw.line(window, (0,0,0), (10+letterSize*letterPosition, 30), (10+letterSize*(letterPosition+1), 30), 2)
                pygame.display.update()