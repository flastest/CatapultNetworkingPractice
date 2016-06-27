import Character, random

class Police(Character.Character):
    
    className = 'Police Officer'
    goal = 'Discover and arrest all criminals in the area'
    abilityDefinition = 'Interrogate other players to find out which are criminals'
    minigameName = 'Interrogation Station'
    abilSuccess = 'You successfully gain information about the target'
    abilLoss = 'You fail to gain any relevant information'

    image = "Officer.png"


    # the minigame involves interrogating different classes...this will involve sprites #kill my    def minigame(window):
    def minigame(self,window):
        # this is the poor person the police interrogates for the minigame
        # equipped with many responses, the police needs to approach with 
        # an open mind and open heart to win the trust of the victim
        class victim:
            
            # these are the responses returned when the officer is getting too pushy
            bad_response = ["That's a little too personal","Back off, pervert!"]

            def __init__(self):
                # how much the victim trusts the police, if this reaches
                # a certain value, the police wins the minigame
                trust_level = 0

            # returns bad_response
            def negative(self):
                return bad_response[random.randint(0,5)]

