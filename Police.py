import Character, random, pygame, time
from pygame.locals import *
pygame.font.init()

class Police(Character.Character):
    
    className = 'Police Officer'
    goal = 'Discover and arrest all criminals in the area'
    abilityDefinition = 'Interrogate other players to find out which are criminals'
    minigameName = 'Interrogation Station'
    abilSuccess = 'You successfully gain information about the target'
    abilLoss = 'You fail to gain any relevant information'

    image = "Officer.png"

    # number of times minigame has been played
    times_played = 0 

    # the minigame involves interrogating different classes...this will involve sprites #killme
    def minigame(self,window):
        # this is the poor person the police interrogates for the minigame
        # equipped with many responses, the police needs to approach with 
        # an open mind and open heart to win the trust of the victim

        font = pygame.font.Font(None,26)
        
        # so there's a defensinve victim an d an onpoen victim and the officer don'tknow whoich one he'ss's getting 
        # this is the soft victim so harsh questioness won't work but soft ones will
        class soft_victim:
            
            # these are the responses returned when the officer is getting too pushy
            bad_response = ["That's a little too personal","Back off, pervert!","Uhh... frowny face","I don't know you well enough to answer that","I don't know..."]

            # these are affirmative responses returned when a soft question is asked
            good_response = ["Of course. I know...","Oh yeah, I remember...","Yup, it was...","Yes! It was...","I remember that..."]

            def __init__(self):
                # how much the victim trusts the police, if this reaches
                # a certain value, the police wins the minigame
                trust_level = 0

            # returns bad_response and good_response
            def negative(self):
                return bad_response[random.randint(0,5)]

            def affirmative(self):
                return good_response[random.randint(0,5)]

            
            # returns false because this victim is defensive
            def isSoft(self):
                return 1
        
        # this victim will respond to the hard questions but not the soft ones
        class hard_victim:
            # these are returned when the officer isn't being threatening enough
            bad_response = ["Why should I answer that?","And why does that matter?","Heck naw I'm not answering that","What does that have to do with me?","What's it to you?"]

            good_response = ["Oh let me tell you all about it...","Anything for you, officer...","Yes!!! It was...","Well it all started when...","I knew, but..."]
            
            def __init__(self):
                # how much the victim trusts the police, if this reaches
                # a certain value, the police wins the minigame
                trust_level = 0

             # returns bad_response or good_response
            def negative(self):
                return bad_response[random.randint(0,5)]
            def affirmative(self):
                return good_response[random.randint(0,5)]
            
            # returns true that this victim is open
            def isSoft(self):
                return 0
            


        # this is the first set of questions that the defensive victim will respond to 
        softlist1 = ["Do you recall seeing a murder anywhere?","Where did you last see the turtle?","When did you last see the loaf of bread?","Who was with the suspicious figure?","How old was she when she left?","Was your bag labeled?"]
        # this is the first set of questions that the open victim will respond to 
        hardlist1 = ["Where did the murder happen, dammit!","Where is the turtle, dammit!","When did you lose the bread, dammit!","Who did you see, dammit!","How old was she, dammit!","Did you label your bag, dammit!"]
        
        softlist2 = ["What did he look like?","Where was this?","Do any of these pictures look familiar?","What can you tell me about him?","When did you notice the taxicab?","Do you know any possible motives?"]
        hardlist2 = ["Who was he, dammit!","Where, dammit!","Did he look like this, dammit!","What do you know about him, dammit!","Did you see the damn taxicab or not, dammit!","You must know, dammit!"]

        softlist3 = ["Does this image ring any bells?","Was she with anyone else?","Did the room have any doors?","Did you see any signs of a leak?","Why were you there?","Did the dog have a party hat?"]
        hardlist3 = ["What does this look like, dammit!","Who else was there, dammit!","How many doors were there, dammit!","Was there a leak, dammit!","Why were you there, dammit!","What was the dog wearing, dammit!"]

        softlist4 = ["What time was it?","How tall was the refridgerator?","When did you notice he was gone?","Was anything else missing?","Did you notice anything else?","How many screams did you hear?"]
        hardlist4 = ["When was it, dammit!","Was the refridgerator big or not, dammit!","When did he leave, dammit!","What did you lose, dammit!","What else happened, dammit!","What did you hear, dammit!"]


        # based on times_played, this function sets the potential questions to 
        # different question lists
        def set_questions(times_played):
            if times_played == 0:
                soft_questions = softlist1.copy()
                hard_questions = hardlist1.copy()
            if times_played == 1:
                soft_questions = softlist2.copy()
                hard_questions = hardlist2.copy()
            if times_played == 2:
                soft_questions = softlist3.copy()
                hard_questions = hardlist3.copy()
            if times_played == 3:
                soft_questions = softlist4.copy()
                hard_questions = hardlist4.copy()
            else:
                soft_questions = softlist1.copy()
                hard_questions = hardlist1.copy()
                times_played = 0

            self.times_played += 1



        # displays questions, takes no input but uses:
        #   hard/soft_questions
        #   fucking pygame
        #   new variable listidx which saves position in question list
        listidx = 0
        def displayQuestions():
            softQ = font.render(soft_questions[listidx],1,(255,255,255))
            hardQ = font.render(hard_questions[listidx],1,(255,255,255))
            screen.blit(softQ,[600,100])
            screen.blit(hardQ,[700,100])

        # clears bottom half of screen
        def clear():
            black = Rect((0,500),(1200,800))
            pygame.draw.rect(window,[0,0,0],black,0)


        # chooses whether to have open or reserved victim
        def set_victim():
            if random.randint(0,1) == 1:
                victim = soft_victim()
            else:
                victim = hard_victim()

        # gets position of mouse click and returns 1 for soft question and 0 for hard 
        # (which question it is shouldn't matter at this point)
        def get_question(pos):
            # checks y position 
            if pos[1] < 613 and pos[1] > 587:
                return 1 # aka "soft"
            if pos[1] < 713 and pos[1] > 687:
                return 0 # aka "hard"
            else:
                return 2 # fucking nothing m8

        # takes response from get_questions and returns victim response
        def ask_question(QAsked):
            if victim.isSoft() == QAsked:
                return victim.affirmative()
            return victim.negative()


        # takes user input and does the actual game
        while True:
            events = pygame.event.get()
            for event in events:

                if event.type == MOUSEMOTION: # just for debugging, this displays coords of mouse
                    title = font.render(str(event.pos), 1, (255,255,255))
                    screen.blit(title, [0,20])
                
                if event.type == MOUSEBUTTONDOWN:
                    mouse = event.pos
                    position = get_question(mouse)
                    print(ask_question(position))


screen = pygame.display.set_mode([1200,800])
test = Police(966)
test.minigame(screen)
