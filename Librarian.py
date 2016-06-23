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

    def minigame(self,window):
        
        # draws shelf from left end of screen to right end of screen
        shelf = Rect((0,600),(1200,20))
        pygame.draw.rect(window, [100,60,40], shelf,0)


        
        class Book:
            
            # gives book starting x pos on the shelf
            def __init__(self,xPos):
                self.x = xPos
            
            def setColor(self,r,g,b):
                self.red = r
                self.green = g
                self.blue = b

            def draw(self):
                # drawing book
                self.book = Rect((self.x, 200),(self.x+75, 400))
                pygame.draw.rect(window, [self.red,self.blue,self.green], self. book, 0)
                
                # the dog shit known as pygame.font
                font = pygame.font.Font(None, 26)
                title = font.render(((44-len(self.text))*" ")+self.text, 1, (0,0,0))
                title = pygame.transform.rotate(title,270)
                
                screen.blit(title, [self.x + 18, 200])

            def addText(self, txt):
                self.text = txt

        
      
        
        # sets number of books to sixteen because it's a minor and sam westerman should know that
        numBooks = 16
        print(numBooks)

        # creates list of random books and random (sex) position
        bookloc = 0
        bookList = []
        
        # list of shitty titles to use
        titleList = ["Github? More like Bukkake","Erotic Sonic Fanfiction", "Comprehensive Guide to Windows 95", "Why Steve Jobs Really Died", "Illuminati Confirmed","Pain in the Ass: Bridge for Beginners","The Middle-Age Testament","Clean Your Hair Out of The Group Shower",
                "Starbucks and the Making of an Empire","Porch Monkey","Human Trafficking for the Elderly","History of Sarah Palin","Breyer Horse Figurine Catalog","How to Make a Meme-Based Lubricant","Celebrating 75 Years","The Significance of 966"]
        titleList2 = ["DSM IV-TR","Delete system32","WISC III","A Comprehensive Guide to the Rorschach","","","","","","","","","","","","Pepe"]

        for b in range(numBooks):
            red = random.randint(50,255)
            green = random.randint(50,255)
            blue = random.randint(50,255)

            print(b)
            i = Book(bookloc)
            i.setColor(red,blue,green)
            i.addText(titleList2[b])
            bookList.append(i)
            i.draw()
            bookloc += 75


       

        pygame.display.update()
        time.sleep(10)
        window.close()



        

screen = pygame.display.set_mode([1200,800])
pygame.display.set_caption("My Window")
kek = Librarian(966)
kek.minigame(screen)

