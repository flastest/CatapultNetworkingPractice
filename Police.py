import Character

class Police(Character.Character):
    
    self.className = 'Police Officer'
    self.goal = 'Discover and arrest all criminals in the area'
    self.abilityDefinition = 'Interrogate other players to find out which are criminals'
    self.minigameName = 'Interrogation Station'
    self.abilSuccess = 'You successfully gain information about the target'
    self.abilLoss = 'You fail to gain any relevant information'


    # the minigame involves interrogating different classes...this will involve sprites #kill myself
    def minigame(self,window):
        

