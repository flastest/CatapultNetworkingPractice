class Character:
    #"""An outline or super-class for each character's individualized class/role""""

    self.className = 'the role of the character'
    self.goal = 'what each character should be trying to do'
    self.abilityDefinition = 'what the ability of the character does'
    self.minigameName = 'the name of the ability and minigame'
    self.abilSuccess = 'what is said when the ability minigame is won'
    self.abilLoss = 'what is said when the ability minigame is won'
    self.gamePoints = 0
    self.playerNumber = -1

    def __init__(self, playerNum):
        self.playerNumber = playerNum

    def __str__(self):
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

    def setAvatar(self, image):
        self.image = image

    def getAvatar(self):
        return self.image

        