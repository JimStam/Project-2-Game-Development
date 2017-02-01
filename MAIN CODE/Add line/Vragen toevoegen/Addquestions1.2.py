
import pygame
import time
import random


red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
black = (0,0,0)


class Game:
    def __init__(self):
        # Set up resolution
        width = 640
        height = 480
        size = (width,height)

        #Start Pygame
        pygame.init()

        #Set the resolution
        self.screen = pygame.display.set_mode(size)

        #Set up the default font
        self.font = pygame.font.Font(None,30)

        #Create Line
        self.Line = Lines()

        #Create Askquestion
        self.Ask = questions.askquestion(self)
        
        #Create player
        self.Player1 = Player(320, 470,red,1)
        self.Player2 = Player(270,470,blue,2)
        self.Player = self.Player1
        self.draw()

    #Ask question
    def ask(self):
            self.Ask.askquestion()

    #Update game logic
    def update_question(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question()
                self.Player = self.Player2
         elif self.Player2.number == 2:
                self.Player.update_question()
                self.Player = self.Player1

    def update_catagoryleft(self):
         if self.Player.number == 1:
                self.Player.update_catagoryleft()
                self.Player = self.Player2
         elif self.Player2.number == 2:
                self.Player.update_catagoryleft()
                self.Player = self.Player1

    def update_catagoryright(self):
         
         if self.Player.number == 1:
                self.Player.update_catagoryright()
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_catagoryright()
                self.Player = self.Player1

    def nextplayer(self):

         if self.Player.number == 1:
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player = self.Player1
            
         

    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)

        #Draw the score text
        #self.score_text = self.font.render("Score: {}".format(self.score),1,(255, 255, 255))
        #self.screen.blit(self.score_text,(16,16))

        #Flip the screen
        pygame.display.flip()

    #The game loop
    def game_loop(self):
        while not process_events():
            for event in pygame.event.get():
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.Ask == "Correct":
                             self.update_question()
                             self.draw()
                        elif self.Ask == "False":
                                self.nextplayer
                                self.draw()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.Ask == "Correct":
                             self.update_question()
                             self.draw()
                        elif self.Ask == "False":
                                self.nextplayer
                                self.draw()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.Ask == "Correct":
                             self.update_question()
                             self.draw()
                        elif self.Ask == "False":
                                self.nextplayer
                                self.draw()

class Player:
   def __init__(self, posX, posY, color,number):
       self.score = 0
       self.posX = posX
       self.posY = posY
       self.radius = 20 
       self.color = color
       self.number = number

   def update_question(self):
        self.posY -= 40
   def update_catagoryleft(self):
        self.posX -= 50

   def update_catagoryright(self):
        self.posX += 50

    
   def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.posX), int(self.posY)), int(self.radius))
                            

class Lines: #Teken de lijnen
    def draw(self,screen):
        pygame.draw.line(screen,red,(320,70),(320,470),10)
        pygame.draw.line(screen,yellow,(270,70),(270,470),10) 
        pygame.draw.line(screen,green,(220,70),(220,470),10)
        pygame.draw.line(screen,blue,(370,70),(370,470),10)
    
class questions:  # vragen op het scherm
    def __init__(self, questions, answer1, answer2, answer3, correct):
        self.questions = questions
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct = correct

        width = 640
        height = 480
        size = (width,height)

        self.screen = pygame.display.set_mode(size)
       
        self.font = pygame.font.Font(None,30)



    def askquestion(self):
        correct = False

        def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar

            width = 640
            height = 480
            size = (width,height)

            self.screen = pygame.display.set_mode(size)
       
            self.font = pygame.font.Font(None,30)

            screen_text = self.font.render(msg, True, color)
            self.screen.blit(screen_text, [height / lokatie1, width / lokatie2])
        
        a = questions(["waar woont Haroon"], ["A : Dordrecht"], ["B : den haag"], ["C : rotterdam"], [pygame.K_a])
        b = questions(["waar woont jawed"], ["A : rotterdam"], ["B : Rijswijk"], ["C : rotterdam"], [pygame.K_b])
        c = questions(["waar woont pietje"], ["A : rotterdam"], ["B : Delft"], ["C : Haarlem"], [pygame.K_a])
        d = questions(["waar woont Anie"], ["A : Zoetermeer"], ["B : Delft"], ["C : rotterdam"], [pygame.K_a])
        e = questions(["waar woont Milad"], ["A : rotterdam"], ["B : Delft"], ["C : Delft"], [pygame.K_b])

        l = [a,b,c,d,e]
        random_selection = random.randint(0, len(l) - 1)


        while not correct:
                # vragen op de scherm krijgen
            self.screen.fill(red)
            messages_to_screen(l[random_selection].questions[0], black, 20, 50)
            messages_to_screen(l[random_selection].answer1[0], black, 20, 5)
            messages_to_screen(l[random_selection].answer2[0], black, 2, 5)
            messages_to_screen(l[random_selection].answer3[0], black, 1, 5)
            messages_to_screen("Kies A , B , C ", black, 9, 4)
            pygame.display.flip()
        # knopjes linken
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if pygame.K_a == l[random_selection].correct[0]:
                            return "True"
                        else:
                            return "False"

                    if event.key == pygame.K_b:
                        if pygame.K_b == l[random_selection].correct[0]:
                            return "True"
                        else:
                            return "False"
                    if event.key == pygame.K_c:
                        if pygame.K_c == l[random_selection].correct[0]:
                            return "True"
                        else:
                            return "False"

    

#Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Give signal to quit
            return True
    return False




#Main program logic
def program():
    game=Game()
    game.game_loop()
 
program()

