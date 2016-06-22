import Character

class Doctor(Character.Character):
    className = 'Doctor'
    goal = 'Cure the virus infecting everybody before it turns deadly.'
    abilityDefinition = 'Performs operations and/or cultures bacteria to learn more about the virus.'
    minigameName = 'Operation' # or Culture Virus
    abilSuccess = 'You successfully perform the operation.' # or 'You successfully culture the bacteria'
    abilLoss = 'The procedure fails.' # 'You fail to learn anything new.'
