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
bg = pygame.image.load('images/bg.png')
#block1 = cathy

cathyB1 = pygame.image.load('images/cathyb1fix.png')
cathyB2 = pygame.image.load('images/cathyb2fix.png')
cathyB3 = pygame.image.load('images/cathyb3fix.png')
cathyB4 = pygame.image.load('images/cathyb4fix.png')
cathyB5 = pygame.image.load('images/cathyb5fix.png')
cathyX = 100
#variables for moving each block


#block2 = hillman
hillmanB1 = pygame.image.load('images/hillmanb1fix.png')
hillmanB2 = pygame.image.load('images/hillmanb2fix.png')
hillmanB3 = pygame.image.load('images/hillmanb3fix.png')
hillmanB4 = pygame.image.load('images/hillmanb4fix.png')
hillmanX = 100

#block3 = posvar
posvarB1 = pygame.image.load('images/posvarb1fix.png')
posvarB2 = pygame.image.load('images/posvarb2fix.png')
posvarB3 = pygame.image.load('images/posvarb3fix.png')
posvarB4 = pygame.image.load('images/posvarb4fix.png')
posvarX = 100
#block4 = wpu
wpuB1 = pygame.image.load('images/wpub1fix.png')
wpuB2 = pygame.image.load('images/wpub2fix.png')
wpuB3 = pygame.image.load('images/wpub3fix.png')
wpuB4 = pygame.image.load('images/wpub4fix.png')
wpuX  = 100
#block5 = benedum
benB1 = pygame.image.load('images/benedumb1fix.png')
benB2 = pygame.image.load('images/benedumb2fix.png')
benB3 = pygame.image.load('images/benedumb3fix.png')
benB4 = pygame.image.load('images/benedumb4fix.png')
benB5 = pygame.image.load('images/benedumb5fix.png')
benB6 = pygame.image.load('images/benedumb6fix.png')
benX = 100


blockY = 75
blockXChange = 0
blockYChange = 5
#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game board
blockStop = False
r,c = 14,24
game_board = [[0 for x in range(r)]for y in range(c)] #24 x 14
x = 100
y =0
print(game_board)
#for c in range (14):

#	for r in range(24):
#		element[c][r] = [x,y]
#		print(element + " |")
#		y += 25
#	x += 25
#	y = 0

for r in range(24):
	for c in range(14):
		game_board[r][c] = [x,y]
		print(game_board[r][c])
		x += 25
	y+= 25
	x = 100

##FUNCTIONS
def cathy(x,y):
	cathyArr = [(x,y)]
	screen.blit(cathyB1, (x,y))
	x=x+25
	cathyArr.append((x,y))
	screen.blit(cathyB2, (x, y))
	cWidth = cathyB2.get_width()
	x = x+25
	cathyArr.append((x,y))
	screen.blit(cathyB3, (x,y))
	x = x-25
	y = y-25
	cathyArr.append((x,y))
	screen.blit(cathyB4, (x,y))
	y = y-25
	cathyArr.append((x,y))
	screen.blit(cathyB5, (x,y))
	return cathyArr

def hillman(x,y):
	hillmanArr = [(x,y)]
	screen.blit(hillmanB1, (x,y))
	x = x+25
	hillmanArr.append((x,y))
	screen.blit(hillmanB2, (x,y))
	x= x+25
	hillmanArr.append((x,y))
	screen.blit(hillmanB3, (x,y))
	x = x+25
	hillmanArr.append((x,y))
	screen.blit(hillmanB4, (x,y))
	return hillmanArr

def posvar(x,y):
	posvarArr = [(x,y)]
	screen.blit(posvarB4, (x,y))
	y = y-25
	posvarArr.append((x,y))
	screen.blit(posvarB2, (x,y))
	x = x+25
	posvarArr.append((x,y))
	screen.blit(posvarB3, (x,y))
	x = x-50
	posvarArr.append((x,y))
	screen.blit(posvarB1, (x,y))
	return posvarArr

def wpu(x,y):
	wpuArr = [(x,y)]
	screen.blit(wpuB3, (x,y))
	x = x+25
	wpuArr.append((x,y))
	screen.blit(wpuB4, (x,y))
	y = y-25
	wpuArr.append((x,y))
	screen.blit(wpuB2, (x,y))
	x = x-25
	wpuArr.append((x,y))
	screen.blit(wpuB1, (x,y))
	return wpuArr

def benedum(x,y):
	benArr = [(x,y)]
	screen.blit(benB1, (x,y))
	x = x+25
	benArr.append((x,y))
	screen.blit(benB2, (x,y))
	x = x+25
	benArr.append((x,y))
	screen.blit(benB3, (x,y))
	x = x+25
	benArr.append((x,y))
	screen.blit(benB4, (x,y))
	y = y-25
	benArr.append((x,y))
	screen.blit(benB6, (x,y))
	x = x-25
	benArr.append((x,y))
	screen.blit(benB5, (x,y))
	return benArr
##game loop
running = True
while running:
	screen.fill((0,0,0))
	screen.blit(bg, (100,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				blockYChange = 5
			if event.key == pygame.K_DOWN:
				blockYChange = 35
			if event.key == pygame.K_LEFT:
				blockXChange = -25
			if event.key == pygame.K_RIGHT:
				blockXChange = 25

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT:
				blockXChange = 0
				blockYChange = 5
	if blockY == 575:
		blockXChange = 0
		blockStop = True
	cathyX += blockXChange
	hillmanX += blockXChange
	posvarX += blockXChange
	wpuX += blockXChange
	benX += blockXChange
	blockY += blockYChange
	if cathyX >= 450:
		cathyX = 450
	if cathyX <= 100 or hillmanX <= 100 or posvarX <= 125 or wpuX <= 100 or benX <= 100:
		cathyX = 100
		hillmanX = 100
		posvarX = 125
		wpuX = 100
		benX = 100
	if hillmanX >= 425:
		hillmanX = 425
	if posvarX >= 475:
		posvarX = 475
	if wpuX >= 475:
		wpuX = 475
	if benX >= 425:
		benX = 425
	if blockY >= 575:
		blockY = 575
	blockCoords = wpu(wpuX, blockY)
	sameX = False
	sameY = False

	if blockStop:
		for block in blockCoords:
			for r in range(24):
				for c in range(14):
					if game_board[r][c][0] == (block[0] -75):
						sameX = True
					if game_board[r][c][1] == block[1]:
						sameY = True
					if sameX and sameY:
						game_board[r][c][0] = -1
						game_board[r][c][1] = -1
					sameX = False
					sameY = False
	print(game_board)


	pygame.display.update()
	pygame.time.delay(100)
