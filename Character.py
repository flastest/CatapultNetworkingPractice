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
        playerNumber = playerNum

    def __str__(self):
        return className

    def getGoal(self):
        return goal
    
    def getAbilityDefinition(self):
        return abilityDefinition
    
    def getAbilityName(self):
        return minigameName
    
    def getMinigameWinText(self):
        return abilSuccess
    
    def getMinigameLossText(self):
        return abilLoss
    
    def getPlayerNumber(self):
        return playerNumber
    
    def getPoints(self, num):
        gamePoints += num
    
    def losePoints(self, num):
        gamePoints -= num

    def setAvatar(self, image):
        image = image

    def getAvatar(self):
        return image

        