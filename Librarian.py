import Character, random, pygame,time
from pygame.locals import *
pygame.font.init()

class Librarian(Character.Character):

    className = 'Librarian'
    goal = 'Seek and organize books while seeking a quiet place to read'
    abilityDefinition = 'Sort the books in this room'
    minigameName = 'Sort books'
    abilSuccess = 'You successfully sort the books'
    abilLoss = 'You fail to sort the books'

    minigameCount = 0

    def minigame(self,window):
        
        
        class Book:
            width = 75

            # gives book starting x pos on the shelf
            def __init__(self,xPos):
                self.x = xPos

            
            def setColor(self,r,g,b):
                self.red = r
                self.green = g
                self.blue = b

            def draw(self):
                # drawing book

                self.book = Rect((self.x, 200),(self.x+self.width, 400))
                pygame.draw.rect(window, [self.red,self.blue,self.green], self. book, 0)
                
                # the dog shit known as pygame.font
                font = pygame.font.Font(None, 26)
                title = font.render(((44-len(self.text))*" ")+self.text, 1, (0,0,0))
                title = pygame.transform.rotate(title,270)
                
                screen.blit(title, [self.x + 18, 200])

            def addText(self, txt):
                self.text = txt

            def setPos(self,deltaX):
                self.x += deltaX

            def getPos(self):
                return self.x

            def isClicked(self,x,y):
                if self.x + 75 > x and self.x < x:
                    if 200 < y and 400 > y:
                        return True
                return False
            
            def getBookWidth(self):
                return self.width

            def toString(self):
                return self.text
        
        
        # draws shelf from left end of screen to right end of screen
        shelf = Rect((0,600),(1200,20))
        pygame.draw.rect(window, [100,60,40], shelf,0)

        # sets number of books to sixteen because it's a minor and sam westerman should know that
        numBooks = 16
        print(numBooks)

        
        
        # list of shitty titles to use
        titleList = ["Github? More like Bukkake","Erotic Sonic Fanfiction", "Comprehensive Guide to Windows 95", "Why Steve Jobs Really Died", "Illuminati Confirmed","Pain in the Ass: Bridge for Beginners","The Middle-Age Testament","Clean Your Hair Out of The Group Shower",
                "Starbucks and the Making of an Empire","Porch Monkey","Human Trafficking for the Elderly","History of Sarah Palin","Breyer Horse Figurine Catalog","How to Make a Meme-Based Lubricant","Celebrating 75 Years","The Significance of 966"]
        titleList2 = ["DSM IV-TR","Delete system32","Cosmopolitan","A Comprehensive Guide to the Rorschach","How to Make a Solar Hooker from Scratch","Julius Caesar Salad","Pokemon Emerald","Lord of the Fries","To Kill a Meme-ing Bird","Of Mice and Memes","Catch-966","Anon in an Anonymous Land",            "Bae-o-wulf","Alice's Adventures in Reddit","Prunes and Prejudice","The Mediocre Gatsby"]
        titleList3 = ["Another Young Adult Vampire Romance Novel","War and Pepe","The Fault in our Apple Devices","The Adventures of Blackberry Phone","Lolita","The Lion King","Nineteen-Eighty-Three-Point-Nine-Six-Six","Gone with the Meme","Pomegranates of Wrath","The CATAPULTry Tales",
                "Billy Joel's Greatest Hits'","The Merchant of Chinatown","Much Ado about Cookies","Less Miserables","Old Man and The Book that Dragged on Forever","Hoarder of the Things"]
        titleList4 = ["Charlotte the Pleb","One Flew Over The Cuckoo's Nest","Twenty Thousand Leagues into the Internet","The Strange Case of Dr. Jekyll and Mr. Mime","A Clockwork Pepe","Call of the Meme","Through the Computer Monitor","All Quiet on the Viral Front",
                "The Lion, The Witch and the Unpacked Suitcase","Love in the Time of Zika","The Prelude/Angry Young Man","Journey to the Center of Walmart","A Midsummer's Night Meme","Uncle Tom's Beach Resort","If I Forget Thee, Jerusalem","Just Start Mushing it Slowly but Erotically"]
        # Other names:
        #   A Wrinkle in Spine、けっけっけっ、二千歳、ぺぺ

        # creates books for the minigame

        # creates list of random books and random (sex) position
        bookloc = 0
        bookList = []

        for b in range(numBooks):
            red = random.randint(50,255)
            green = random.randint(50,255)
            blue = random.randint(50,255)

            print(b)
            i = Book(bookloc)
            i.setColor(red,blue,green)
            # does a different set of books times each time minigame is played
            if self.minigameCount == 0:
                i.addText(titleList[b])
            if self.minigameCount == 1:
                i.addText(titleList2[b])
            if self.minigameCount == 2:
                i.addText(titleList3[b])
            if self.minigameCount == 3:
                i.addText(titleList4[b])    
            bookList.append(i)
            i.draw()
            bookloc += 75

        # adds counter to minigame so same books aren't used again
        self.minigameCount += 1    


        # now for the actual playing part of the minigame

        # getClickedBook takes a position and returns the clicked book
        def getClickedBook(pos):
            self.clickX = pos[0]
            self.clickY = pos[1]
            if self.clickY < 400 and self.clickY > 200:
                for x in range(16):
                    if (x + 1) * bookList[x].getBookWidth() > self.clickX:
                        return bookList[x]
            
        def switchBooks(book1,book2):
            firstX = book1.getPos()
            secondX = book2.getPos()
            book1.setPos(secondX)
            book2.setPos(firstX)
            book1.draw()
            book2.draw()

        
        #print("幽門はミーム")
        pygame.display.update()

        # user input stuff goes here
        numClicks = 0
        while True:
            # takes all events
            events = pygame.event.get()
            for event in events:
                # if user clicks a book, the computer remembers which book was clicked
                if event.type == MOUSEBUTTONDOWN and numClicks == 0:
                    mouse = event.pos
                    self.click1 = getClickedBook(mouse)
                    print(self.click1.toString())
                    numClicks = 1
                # checks for second click 
                if event.type == MOUSEBUTTONDOWN and numClicks == 1:
                    mouse = event.pos
                    self.click2 = getClickedBook(mouse)
                    print(self.click2.toString())
                    numClicks = 0
                    switchBooks(self.click1,self.click2)

                # ends game if user quits
                if event.type == QUIT:
                    return 
            pygame.display.update()    



       

        

screen = pygame.display.set_mode([1200,800])
pygame.display.set_caption("乳酸菌と解剖と肝臓")
kek = Librarian(966)
kek.minigame(screen)


