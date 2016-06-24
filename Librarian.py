import Character, random, pygame,time
from pygame.locals import *

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
                self.book = Rect((self.x, 200),(self.x+75, 400))
                pygame.draw.rect(window, [self.red,self.blue,self.green], self. book, 0)
                self.title = pygame.font.render(self.text, True, BLACK)
                self.title = pygame.transform.rotate(title,90)
                screen.blit(title, [self.x + 37, 300])

            def addText(self, txt):
                self.text = txt

        # sets number of books
        numBooks = 16
        print(numBooks)

        # creates list of random books and random position
        bookloc = 0
        bookList = []
        for b in range(numBooks):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            i = Book(bookloc)
            i.setColor(red,blue,green)
            i.addText("yolo")
            bookList.append(i)
            i.draw()
            bookloc += 75




        pygame.display.flip()
        time.sleep(2)
        window.close()



        

screen = pygame.display.set_mode([1200,800])
pygame.display.set_caption("My Window")
kek = Librarian(966)
kek.minigame(screen)

