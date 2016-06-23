import Character
import pygame, clock, random

class Burglar(Character.Character):

    className = 'Burglar'
    goal = 'Steal as much as you can, while evading detection.'
    abilityDefinition = 'Pick the lock that stands in your way.'
    minigameName = 'Lockpick'
    abilSuccess = 'You successfully pick the lock.'
    abilLoss = 'You fail to pick the lock.'
    image = 'Robber.png'
    timeLimit = 100 # minigame time limit, feel free to change as needed

    def minigame(self, t):
        minigameWon = False
        minigameLost = False
        startTime = time.clock()
        
        pygame.init()
        window = pygame.display.set_mode([1200,800])
        pygame.display.set_caption('Picking lock . . .')

        ended = False
        canOpen = False
        while not minigameWon and not minigameLost:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    ended = True
                    break
                if event.type == KEYDOWN:
                    if event.key == K_LSHIFT:
                        self.isUprCase = False
                    if event.key == K_LEFT:
                        pass
                    if event.key == K_RIGHT:
                        pass
                    if event.key == K_UP:
                        pass
                    if event.key == K_DOWN:
                        pass
            window.fill((170,170,170))
            pygame.display.Rect()
            pygame.display.update()
            for i in range(5):
                count = 0
                if pin[i] == pos[i]:
                    count += 1
                if count == 5:
                    canOpen = True
            if time.clock() > startTime + self.timeLimit:
                minigameLost = True
            if ended:
                pygame.display.quit()
                break
        if minigameWon or minigameLost:
            self.showEndScreen(window, minigameWon, t)