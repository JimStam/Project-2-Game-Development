import pygame
import time
import random
pygame.init()

white  = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption('Quiz')


font = pygame.font.SysFont(None,30)

class questions():
    def __init__(self,questions,answers):
        self.questions=questions
        self.answers=answers


q = questions(["tttt"],["ppp"])
def messages_to_screen(msg,color,lokatie1,lokatie2):# massage hoe hij er uit moet zien en waar
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_hight/lokatie1, display_width/lokatie2])



def  gameLoop ():

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.fill(red)
        messages_to_screen(q.answers[0],black,10,9)
        messages_to_screen("Kies A , B , C ", black,9,4)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                   messages_to_screen("Gooooooooooos", black, 5, 9)


                if event.key == pygame.K_b:
                    gameExit = True


gameLoop()

