from images import *

class Character:
    #"""An outline or super-class for each character's individualized class/role""""

    className = 'the role of the character'
    goal = 'what each character should be trying to do'
    abilityDefinition = 'what the ability of the character does'
    minigameName = 'the name of the ability and minigame'
    abilSuccess = 'what is said when the ability minigame is won'
    abilLoss = 'what is said when the ability minigame is won'
    gamePoints = 0
    playerNumber = -1

    def __init__(self, playerNum):
        self.playerNumber = playerNum

    def getName(self):
        return self.className

    def getGoal(self):
        return self.goal
    
    def getAbilityDefinition(self):
        return self.abilityDefinition
    
    def getAbilityName(self):
        return self.minigameName
    
    def getMinigameWinText(self):
        return self.abilSuccess
    
    def getMinigameLossText(self):
        return self.abilLoss
    
    def getPlayerNumber(self):
        return self.playerNumber
    
    def getPoints(self, num):
        self.gamePoints += num
    
    def losePoints(self, num):
        self.gamePoints -= num

    def setAvatar(self, avatar):
        self.image = avatar

    def getAvatar(self):
        return self.image

    def drawCharacter(self,posX,posY,win):
        image = images(self.image)
        image.display(posX,posY,win)

        