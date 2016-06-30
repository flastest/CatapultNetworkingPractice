import Character, random, pygame,time
from pygame.locals import *
pygame.font.init()

# LIFE HACKS:
# CTRL-K then CTRL-U to uncomment 
# CTRL-K the CTRLY-C to comment
class Librarian(Character.Character):

    className = 'Librarian'
    goal = 'Seek and organize books while seeking a quiet place to read'
    abilityDefinition = 'Sort the books in this room by color from red to pink'
    minigameName = 'Sort Books'
    abilSuccess = 'You successfully sort the books'
    abilLoss = 'You fail to sort the books'
    image = 'Librarian.png'

    minigameCount = 0

    def display(self,window,coordinates):
        window.blit(pygame.image.load(self.image),(coordinates[0],coordinates[1]))

    def minigame(self,window):
        pygame.display.set_caption(self.minigameName)

        # draws shelf from left end of screen to right end of screen
        shelf = Rect((0,600),(1200,20))
        pygame.draw.rect(window, [100,60,40], shelf,0)

        # draws instructions
        font = pygame.font.Font(None, 26)
        guide = font.render(self.abilityDefinition, 1, (255,255,255))
        screen.blit(guide,[0,150])
        
        # initializes timer
        startTime = time.clock()


        class Book:

            width = 75

            # gives book starting x pos on the shelf
            def __init__(self,xPos):
                self.x = xPos

            
            def setColor(self,list):
                self.red = list[0]
                self.green = list[1]
                self.blue = list[2]

            # draws book 
            def draw(self):
                self.book = Rect((self.x, 200),(self.width, 400))
                pygame.draw.rect(window, [self.red,self.green,self.blue], self.book, 0)
                
                # the dog shit known as pygame.font
                font = pygame.font.Font(None, 26)
                title = font.render(((44-len(self.text))*" ")+self.text, 1, (0,0,0))
                title = pygame.transform.rotate(title,270)
                
                screen.blit(title, [self.x + 18, 200])

            def addText(self, txt):
                self.text = txt

            def setPos(self,newX):
                self.x = newX

            def getPos(self):
                return self.x

            def isClicked(self,x,y):
                if self.x + 75 > x and self.x < x:
                    if 200 < y and 600 > y:
                        return True
                return False
            
            def getBookWidth(self):
                return self.width

            def toString(self):
                return self.text
            
            def getColor(self):
                return (self.red,self.green,self.blue)
        
        

        # sets number of books to sixteen because it's a minor and sam westerman should know that
        numBooks = 16

        # list of shitty titles to use
        titleList = ["The Horrors of Github","A Brief History of Fanfiction", "Comprehensive Guide to Windows 95", "Why Steve Jobs Really Died", "Illuminati Confirmed","Bridge for Beginners, Abridged","The Middle-Age Testament","How to Clean Your Bathroom",
                "Starbucks and the Making of an Empire","Porch Monkey","Using the Internet for the Elderly","History of Sarah Palin","Breyer Horse Figurine Catalog","How to Meme","Celebrating 75 Years","The Significance of 966"]
        titleList2 = ["DSM IV-TR","Deleting System32","Cosmopolitan","A Comprehensive Guide to the Rorschach","Error 404, Book not found","Julius Caesar Salad","Pokemon Emerald","Lord of the Fries","To Kill a Meme-ing Bird","Of Mice and Memes","Catch-42","Anon in an Anonymous Land",                         "Bae-o-wulf","Alice's Adventures in Reddit","Prunes and Prejudice","The Mediocre Gatsby"]
        titleList3 = ["Another Young Adult Vampire Romance Novel","War and Pepe","The Fault in our Apple Devices","The Adventures of Blackberry Phone","A Complete History of the Catapult","The Lion King","1983.5","Gone with the Meme","Pomegranates of Wrath","The CATAPULTry Tales",
                "Billy Joel's Greatest Hits'","The Merchant of Chinatown","Much Ado about Cookies","Less Miserables","Old Man and The Book that Dragged on Forever","Hoarder of the Things"]
        titleList4 = ["Charlotte the Pleb","One Flew Over The Catamonkey's Nest","Twenty Thousand Leagues into the Internet","The Strange Case of Dr. Jekyll and Mr. Mime","A Clockwork Pepe","Call of the Meme","Through the Computer Monitor","All Quiet on the Viral Front",
                "The Lion, The Witch and the Unpacked Suitcase","Love in the Time of Zika","The Prelude/Angry Young Man","Journey to the Center of Walmart","Much Ado About Memes","Uncle Tom's Beach Resort","If I Forget Thee, Jerusalem","Just Do It, A Biography of Shia LeBeouf"]
        # Other names:
        #   A Wrinkle in Spine、けっけっけっ、二千歳、ぺぺ

        # this below is the key for the game, it's shuffled every minigame to produce a random scenario
        colorList = [(170,0,0),(225,15,0),(232,94,16),(255,132,29),(255,200,15),(255,248,33),(191,255,33),(110,255,33),(16,205,6),(70,226,180),(41,177,193),(24,135,180),(45,65,209),(113,80,217),(143,56,225)      ,(182,50,205)]
        
        # creates books for the minigame by initializing all the book objects and 
        # assigning them random colors from shuffledColors
        bookloc = 0 # location of book to be placed
        bookList = []
        shuffledColors = colorList.copy()
        random.shuffle(shuffledColors)
        
        # this is for debugging, just rigging colors lol
        # shuffledColors = [(182,50,205),(225,15,0),(232,94,16),(255,132,29),(255,200,15),(255,248,33),(191,255,33),(110,255,33),(16,205,6),(70,226,180),(41,177,193),(24,135,180),(45,65,209),(113,80,217),(143,56,225),(170,0,0)]

        for b in range(numBooks): 
            # print(shuffledColors[b])
            colorr = shuffledColors[b]

            i = Book(bookloc)
            i.setColor(colorr) # sets random color to book

            # does a different set of books times each time minigame is played
            if self.minigameCount == 0:
                i.addText(titleList[b])
            if self.minigameCount == 1:
                i.addText(titleList2[b])
            if self.minigameCount == 2:
                i.addText(titleList3[b])
            if self.minigameCount == 3:
                i.addText(titleList4[b])    
            else:
                i.addText(titleList[b])
                self.minigameCount = 0

            
            bookList.append(i)
            i.draw()
            bookloc += 75

        # adds counter to minigame so same books aren't used again
        self.minigameCount += 1 


        # now for the actual playing part of the minigame

        # # getClickedBook takes a position and returns the clicked book
        # def getClickedBook(pos):
        #     self.clickX = pos[0]
        #     self.clickY = pos[1]
        #     if self.clickY < 600 and self.clickY > 200:
        #         for x in range(16):
        #             if (x + 1) * bookList[x].getBookWidth() > self.clickX:
        #                 return bookList[x]

        # returns bookList idx of clicked book
        def getBookIdx(pos):
            self.clickX = pos[0]
            self.clickY = pos[1]
            if self.clickY < 600 and self.clickY > 200:
                for x in range(16):
                    if (x + 1) * bookList[x].getBookWidth() > self.clickX:
                        return x
        
        # uses bookList indexes to switch books
        def switchIdx(idx1,idx2):
            book1 = bookList[idx1]
            book2 = bookList[idx2]
            pos1 = book1.getPos()
            pos2 = book2.getPos()
            # change positions of books
            book1.setPos(pos2)
            book2.setPos(pos1)
            # change list positions
            bookList[idx2] = book1
            bookList[idx1] = book2
            book1.draw()
            book2.draw()

        # def switchBooks(book1,book2):
        #     firstX = book1.getPos()
        #     print("switch this!!",firstX)
        #     secondX = book2.getPos()
        #     print("and this!!",secondX)
        #     book1.setPos(secondX)
        #     book2.setPos(firstX)
        #     book1.draw()
        #     book2.draw()

        
        #print("幽門はミーム")
            pygame.display.update()

        # checks if books are in color order
        def inOrder():
            counter = 0
            for x in range(16):
                # print("comparing",shuffledColors[x],"and",colorList[x])   # debugging
                if bookList[x].getColor() == colorList[x]:
                    counter += 1
            if counter == 16:
                return True
            return False


        # user input stuff goes here
        numClicks = 0
        unordered = True
        while unordered:
            # initializes font and other reusable text things
            clear = Rect((0,0),(1200,150))
            font = pygame.font.Font(None, 26)
            # draws the timer
            remainingTime = round(40 - (time.clock()-startTime)) # Starting time for timer goes here (30 or something)
            pygame.draw.rect(window,[0,0,0],clear,0)
            currentTime = font.render(str(remainingTime),1,(255,255,255))
            screen.blit(currentTime,[1165,8])

            # checks if time hasn't yet run out
            if remainingTime <= 0:
                return


            # takes all inputted events and figures out what to do with them
            events = pygame.event.get()
            for event in events:
                
                # displays coord of mouse
                if event.type == MOUSEMOTION:
                    pass
                   # title = font.render(str(event.pos), 1, (255,255,255))
                   # screen.blit(title, [0,20])
                
                # checks for second click 
                if event.type == MOUSEBUTTONDOWN and numClicks == 1:
                    mouse = event.pos
                    # checks to make sure a book is clicked
                    if mouse[1] > 200 and mouse[1] < 600:
                        numClicks = 2
                        self.click2 = getBookIdx(mouse) 
                        switchIdx(self.click2,self.click1)
                                       
                # if user clicks a book, the computer remembers which book was clicked
                if event.type == MOUSEBUTTONDOWN and numClicks == 0:
                    mouse = event.pos
                    # checks to make sure a book is clicked
                    if mouse[1] > 200 and mouse[1] < 600:
                        self.click1 = getBookIdx(mouse) 
                        numClicks = 1
                
                # checks for third click to reset 
                if event.type == MOUSEBUTTONDOWN and numClicks == 2:
                    self.click1 = 0
                    self.click2 = 0
                    
                    mouse = event.pos
                    #print("third click is at",mouse)
                    numClicks = 0
                
                if inOrder():
                    unordered = False
                    break

                # ends game if user quits
                if event.type == QUIT:
                    return 
                pygame.display.update()    

                

       

        

#screen = pygame.display.set_mode([1200,800])

#kek = Librarian(966)
#kek.minigame(screen)
# time.sleep(1)
# kek.minigame(screen)


