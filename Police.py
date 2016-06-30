import Character, random, pygame, time
from pygame.locals import *
pygame.font.init()

class Police(Character.Character):
    
    className = 'Police Officer'
    goal = 'discover and arrest all criminals in the area'
    abilityDefinition = 'interrogate other players to find out which are criminals'
    minigameName = 'Interrogation Station'
    abilSuccess = 'You successfully gain information about the target'
    abilLoss = 'You fail to gain any relevant information'

    image = "Officer.png"
    victimImg = "victim.png"

    # number of times minigame has been played
    times_played = 0 

    # the minigame involves interrogating different classes...this will involve sprites #killme
    def minigame(self,window,thisVariable):
        # this is the poor person the police interrogates for the minigame
        # equipped with many responses, the police needs to approach with 
        # an open mind and open heart to win the trust of the victim

        # initializes font and draws victim
        font = pygame.font.Font(None,30)
        # bigger font for names
        nameFont = pygame.font.Font(None,40)
        
        # oh crap english is so cool victim + image = victimage 
        victimage = pygame.image.load(self.victimImg)
        window.blit(victimage,(320,40))
        pygame.display.flip()

        # sets up text box
        white_border = Rect(((0,500),(1200,800)))
        pygame.draw.rect(window,[255,255,255],white_border,0)
        pygame.display.update()

        # initializes timer
        startTime = time.clock()
        
        
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
                self.trust_level = 0

            # returns bad_response and good_response
            def negative(self):
                return self.bad_response[random.randint(0,4)]

            def affirmative(self):
                return self.good_response[random.randint(0,4)]
                
            # returns false because this victim is defensive
            def isSoft(self):
                return 1
            
            # This is like the officer's score
            def addTrust(self):
                self.trust_level += 1

            def getTrust(self):
                return self.trust_level
        
        # this victim will respond to the hard questions but not the soft ones
        class hard_victim:
            # these are returned when the officer isn't being threatening enough
            bad_response = ["Why should I answer that?","And why does that matter?","Heck naw I'm not answering that","What does that have to do with me?","What's it to you?"]

            good_response = ["Oh let me tell you all about it...","Anything for you, officer...","Yes!!! It was...","Well it all started when...","I knew, but..."]
            
            def __init__(self):
                # how much the victim trusts the police, if this reaches
                # a certain value, the police wins the minigame
                self.trust_level = 0

             # returns bad_response or good_response
            def negative(self):
                return self.bad_response[random.randint(0,4)]
            def affirmative(self):
                return self.good_response[random.randint(0,4)]
            
            # returns true that this victim is open
            def isSoft(self):
                return 0
            
            # This is like the officer's score
            def addTrust(self):
                self.trust_level += 1
            def getTrust(self):
                return self.trust_level
            


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
        # def set_questions(times_played):
        if self.times_played == 0:
            soft_questions = softlist1.copy()
            hard_questions = hardlist1.copy()
        if self.times_played == 1:
            soft_questions = softlist2.copy()
            hard_questions = hardlist2.copy()
        if self.times_played == 2:
            soft_questions = softlist3.copy()
            hard_questions = hardlist3.copy()
        if self.times_played == 3:
            soft_questions = softlist4.copy()
            hard_questions = hardlist4.copy()
        else:
            soft_questions = softlist1.copy()
            hard_questions = hardlist1.copy()
            self.times_played = 0

        self.times_played += 1

        # updates the name in the corner
        def drawTitle():
            title_white = Rect((0,420),(300,80))
            title_black = Rect((10,430),(280,70))
            pygame.draw.rect(window,[255,255,255],title_white,0)
            pygame.draw.rect(window,[0,0,0],title_black,0)

        def clearTitle():
            title_black = Rect((10,430),(280,70))
            pygame.draw.rect(window,[0,0,0],title_black,0)


        # displays questions, takes no input but uses:
        #   hard/soft_questions
        #   fucking pygame
        #   new variable listidx which saves position in question list
        listidx = 0
        def displayQuestions():
            softQ = font.render(soft_questions[listidx],1,(255,255,255))
            hardQ = font.render(hard_questions[listidx],1,(255,255,255))
            screen.blit(softQ,[100,600])
            screen.blit(hardQ,[100,700])

        # clears bottom half of screen (aka the text box)
        def clear():
            black = Rect((10,510),(1180,780))
            pygame.draw.rect(window,[0,0,0],black,0)

        # clears top left corner of screen (actually entire top)
        def clearCoords():
            corner_black = Rect((0,0),(1200,100))
            pygame.draw.rect(window,[0,0,0],corner_black,0)


        # chooses whether to have open or reserved victim
        if random.randint(0,1) == 1:
            victim = soft_victim()
        else:
            victim = hard_victim()
        #set_questions(self.times_played)

        # gets position of mouse click and returns 1 for soft question and 0 for hard 
        # (which question it is shouldn't matter at this point)
        def get_question(pos):
            # checks y position 
            if pos[1] < 650 and pos[1] > 550:
                return 1 # aka "soft"
            if pos[1] < 750 and pos[1] > 650:
                return 0 # aka "hard"
            else:
                return 2 # fucking nothing m8

        # takes response from get_questions and returns victim response
        def ask_question(QAsked):
            if victim.isSoft() == QAsked:
                displayResponse(victim.affirmative())
                victim.addTrust()
            else:
                displayResponse(victim.negative())

        # takes response of victim from prior function and displays it
        def displayResponse(response):
            response_to_display = font.render(response,1,(255,255,255))
            screen.blit(response_to_display,[100,650])


        # this function takes a name and displays it in the title box
        def drawName(name):
            clearTitle()
            text_to_draw = nameFont.render(name,1,(255,255,255))
            screen.blit(text_to_draw,[30,455])

        # counter for successful clicks...
        turn_counter = 0

        # starts off with narrator giving directions
        drawTitle()
        clear()
        drawName("Narrator") 
        instructions = "You have captured a victim! Now is your chance to interrogate them."
        instructions2 = "The victim will only respond to certain questions. Assess the nature "
        instructions3 = "of the victim and ask questions they will answer."
        inst3 = "Click Anywhere to Play!!!"
        
        first_instructions = font.render(instructions,1,(255,255,255))
        second_instructions = font.render(instructions2,1,(255,255,255))
        third_instructions = font.render(instructions3,1,(255,255,255))
        play = font.render(inst3,1,(255,255,255))
        screen.blit(first_instructions,[100,570])
        screen.blit(second_instructions,[100,630])
        screen.blit(third_instructions,[100,660])
        screen.blit(play,[100, 720])

        pygame.display.update()
        
        # a boolean to determine whether it's the police's turn
        # to not click anywhere to continue
        pojito = 0 # 0 means click anywhere, 1 means click in box is needed, 2 means something else

        # takes user input and does the actual game
        while True:
            
            clearCoords()

            # draws timer
            remainingTime = round(40 - (time.clock()-startTime))
            currentTime = font.render(str(remainingTime),1,(255,255,255))
            screen.blit(currentTime,[1165,8])

            # checks if time hasn't yet run out
            if remainingTime <= 0:
                print(self.abilLoss)
                return
                
            
            events = pygame.event.get()
            
            for event in events: ## IN THE CASE OF POJITO AND A CLICK BEING COMMITTED, NOTHING SHOULD HAPPEN!!

                if event.type == MOUSEMOTION: # just for debugging, this displays coords of mouse
                    title = font.render(str(event.pos), 1, (255,255,255))
                    screen.blit(title, [0,20])
                
                # end cases for winning game
                if listidx > 5:
                    if victim.getTrust() > 4:
                        self.showEndScreen(window,True,thisVariable) # <<<   <<<
                        return                  # end cases
                    else:                       # <<<   <<<
                        self.showEndScreen(window,False,thisVariable)
                        return 
                
                # single case for the narrator, anywhere can be clicked to continue
                if event.type == MOUSEBUTTONDOWN and turn_counter == 0:
                    turn_counter += 1
                    pojito = 1
                    #pojito = True # now police's turn to click in certain area

                
                
                
                if event.type == MOUSEBUTTONDOWN and pojito == 0: # this should be the victim's turn
                    print(turn_counter)

                    
                    # now victim responds and click anywhere to continue
                    clear()
                    clearTitle()
                    drawName("Victim")
                    print("answer")
                    mouse = event.pos
                    clickedQ = get_question(mouse)  # returns 1 for soft question, 0 for hard Q
                                                    # or 2 for neither
                    ask_question(clickedQ)
                    
                        
                    # if the click is on the response panel, a click will not trigger question
                    
                    print("click to proceed")
                    turn_counter += 1
                    pygame.display.update() 
                    
                    pojito = 1 
                
                

                # trying new approach...this means it's the officer's turn to select a question
                if event.type == MOUSEBUTTONDOWN and pojito == 2: #and event.pos[1] > 550 and event.pos[1] < 750: #and turn_counter % 2 != 0:
                    clear()
                    clearTitle()
                    drawName("Officer")
                    displayQuestions()
                    mouse = event.pos
                    
                    listidx += 1
                    print("ask")
                    pygame.display.update() 
                    
                    pojito = 0
                        
                                       
                if pojito == 1:
                    pojito = 2
                        
                if event.type == QUIT:
                    return 
            
                pygame.display.update()

    def showRules(self, window, t = 5):
        pygame.init()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill([255,255,255])
            font = pygame.font.Font(None, 36)
            goal = 'Your objective is to ' + self.getAbilityDefinition()
            text1 = font.render(goal, 1, (0,0,0))
            countdown = font.render('Minigame starting in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text1, (10,10))
            window.blit(countdown, (10, 100))
            pygame.display.update()
            time.sleep(1)
            pygame.display.set_caption(self.minigameName)
        self.minigame(window, t)

    def showEndScreen(self, window, hasWon, t):
        self.won = hasWon
        if hasWon:
            words = self.getMinigameWinText()
        else:
            words = self.getMinigameLossText()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill((255,255,255))
            font = pygame.font.Font(None, 36)
            text = font.render(words, 1, (0,0,0))
            countdown = font.render('Returning to the main game in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text, (10,10))
            window.blit(countdown, (10, 100))
            pygame.display.update()
            time.sleep(1)

screen = pygame.display.set_mode([1200,800])
test = Police(966)
test.showRules(screen)
