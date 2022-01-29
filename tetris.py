import pygame
import random
import time
import math
import sys
import PIL
from pygame import mixer
from PIL import Image
#initialize the pygame
pygame.init()

screen = pygame.display.set_mode((600,600))

#block1 = cathy

cathyB1 = pygame.image.load('images/cathyb1fix.png')
cathyB2 = pygame.image.load('images/cathyb2fix.png')
cathyB3 = pygame.image.load('images/cathyb3fix.png')
cathyB4 = pygame.image.load('images/cathyb4fix.png')
cathyB5 = pygame.image.load('images/cathyb5fix.png')

#block2 = hillman
hillmanB1 = pygame.image.load('images/hillmanb1fix.png')
hillmanB2 = pygame.image.load('images/hillmanb2fix.png')
hillmanB3 = pygame.image.load('images/hillmanb3fix.png')
hillmanB4 = pygame.image.load('images/hillmanb4fix.png')
#block3 = posvar
posvarB1 = pygame.image.load('images/posvarb1fix.png')
posvarB2 = pygame.image.load('images/posvarb2fix.png')
posvarB3 = pygame.image.load('images/posvarb3fix.png')
posvarB4 = pygame.image.load('images/posvarb4fix.png')
#block4 = wpu
wpuB1 = pygame.image.load('images/wpub1fix.png')
wpuB2 = pygame.image.load('images/wpub2fix.png')
wpuB3 = pygame.image.load('images/wpub3fix.png')
wpuB4 = pygame.image.load('images/wpub4fix.png')
#block5 = benedum
benB1 = pygame.image.load('images/benedumb1fix.png')
benB2 = pygame.image.load('images/benedumb2fix.png')
benB3 = pygame.image.load('images/benedumb3fix.png')
benB4 = pygame.image.load('images/benedumb4fix.png')
benB5 = pygame.image.load('images/benedumb5fix.png')
benB6 = pygame.image.load('images/benedumb6fix.png')

#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

##FUNCTIONS
def cathy(x,y):

    screen.blit(cathyB1, (x,y))
    x=x+25
    screen.blit(cathyB2, (x, y))
    cWidth = cathyB2.get_width()
    x = x+25
    screen.blit(cathyB3, (x,y))
    x = x-25
    y = y-25
    screen.blit(cathyB4, (x,y))
    y = y-25
    screen.blit(cathyB5, (x,y))

def hillman(x,y):
    screen.blit(hillmanB1, (x,y))
    x = x+25
    screen.blit(hillmanB2, (x,y))
    x= x+25
    screen.blit(hillmanB3, (x,y))
    x = x+25
    screen.blit(hillmanB4, (x,y))

def posvar(x,y):
    screen.blit(posvarB4, (x,y))
    y = y-25
    screen.blit(posvarB2, (x,y))
    x = x+25
    screen.blit(posvarB3, (x,y))
    x = x-50
    screen.blit(posvarB1, (x,y))
def wpu(x,y):
    screen.blit(wpuB3, (x,y))
    x = x+25
    screen.blit(wpuB4, (x,y))
    y = y-25
    screen.blit(wpuB2, (x,y))
    x = x-25
    screen.blit(wpuB1, (x,y))

def benedum(x,y):
    screen.blit(benB1, (x,y))
    x = x+25
    screen.blit(benB2, (x,y))
    x = x+25
    screen.blit(benB3, (x,y))
    x = x+25
    screen.blit(benB4, (x,y))
    y = y-25
    screen.blit(benB6, (x,y))
    x = x-25
    screen.blit(benB5, (x,y))
##game loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
	       if event.type == pygame.QUIT:
	              pygame.quit()
	              exit()
    cathy(300,500)
    hillman(420,500)
    posvar(300, 200)
    wpu(100,100)
    benedum(300, 400)



    pygame.display.update()
