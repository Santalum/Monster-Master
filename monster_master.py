#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
#import sys
import time
import random
from pygame.locals import *

random.seed()
pygame.init()
pygame.display.set_caption("Monster Master")
myfont = pygame.font.SysFont("TakaoMincho", 40)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bg = black
masterHealth = 3
cateyeHeight = 16
cateyeWidth = 18
catWidth = 64
catHeight = 48

pressed_down = False
pressed_left = False
pressed_right = False
pressed_up = False
bgMode = 0
wallMode = 0
fps = 60
dispWidth = 800  # 1366  # 800  # 1366
dispHeight = 600  # 768  # 600  # 768
wallSize = 32
cellSize = 16
x_move = 0
master_x = dispWidth / 2 - 16
master_y = dispHeight / 2 - 32
master_direction = 0
show_inventory = False
tickcount = 0
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))

#gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
#	pygame.FULLSCREEN)
#image defines
#master
master1Img = pygame.image.load('sprite/master/master1.png')		# master sprite
master2Img = pygame.image.load('sprite/master/master2.png')		# master sprite
sword0Img = pygame.image.load('sprite/weapon/sword/0.png')		# master sprite
#background
bg0Img = pygame.image.load('level/0f.png')
bg1Img = pygame.image.load('level/1.png')
bg2Img = pygame.image.load('level/2.png')
bg3Img = pygame.image.load('level/3.png')
bg4Img = pygame.image.load('level/4.png')
#mushroom
mush0Img = pygame.image.load('sprite/mushroom/0.png')
mush1Img = pygame.image.load('sprite/mushroom/1.png')
mush2Img = pygame.image.load('sprite/mushroom/2.png')
mush3Img = pygame.image.load('sprite/mushroom/3.png')
#wall
wall0Img = pygame.image.load('sprite/wall/0.png')
#monster
monster1Img = pygame.image.load('sprite/monster/0.png')
floor0Img = pygame.image.load('sprite/floor/3.png')
orb = pygame.image.load('sprite/item/orb.png')
#nekodearu
neko1Img = pygame.image.load('sprite/cat/neko1.png')
neko2Img = pygame.image.load('sprite/cat/neko2.png')


def text_objects(text, font):
	textSurface = font.render(text, True, green)
	return textSurface, textSurface.get_rect()


def introMenu():
	gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
		pygame.FULLSCREEN)
	pygame.mixer.music.load("music/xm/oval.xm")
	pygame.mixer.music.play(1, 0)
	intro_screen('Static Studio', 3, 0)
	intro_screen('Proudly Presents', 3, 1)
	intro_screen('Monster Master', 6, 2)
	#masterMove = distance / (13*fps)
	menu_screen((dispHeight / 2) / (13 * fps))	 # 0.34871794871)


def intro_screen(text, showTime, ndx):
	largeText = pygame.font.Font('freesansbold.ttf', (dispWidth / 10))
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((dispWidth / 2), (master_y))
	gameDisplay.fill(black)
	gameDisplay.blit(bg0Img, [0, 0], (0, ndx * 768, 1366, 768))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(showTime)


def menu_screen(masterMove):
	for x in range(0, (13) * fps):
		#gameDisplay.fill(green)
		gameDisplay.blit(bg1Img, [0, 0], (0, 3 * 768, 1366, 768))
		master(master_x, dispHeight - x * masterMove, 1)
		pygame.display.update()
		clock.tick(fps)
	gameDisplay.blit(bg0Img, [0, 0], (0, 3 * 768, 1366, 768))
	master(master_x, master_y, 0)
	pygame.display.update()
	time.sleep(0.2)


def master(x, y, direction):
	if direction == 0:  # down
		gameDisplay.blit(master1Img, (x, y), (0, 0, 32, 64))
	elif direction == 1:  # up
		gameDisplay.blit(master1Img, (x, y), (32, 0, 32, 64))
	elif direction == 2:  # right
		gameDisplay.blit(master1Img, (x, y), (64, 0, 32, 64))
	elif direction == 3:  # left
		gameDisplay.blit(master1Img, (x, y), (96, 0, 32, 96))


def generateLevel():
	for x in range(0, dispWidth / 128 + 1):
		for y in range(0, dispHeight / 128 + 1):
			gameDisplay.blit(floor0Img, (x * 128, y * 128))
	# pygame.display.update ()


class Master:
	def __init__(self):
		# Class Attributes ---
		# Master position
		self.x = 0
		self.y = 0
		# Hitpoints
		self.hitpoints = 3
		# Master's vector
		self.change_x = 0
		self.change_y = 0
		self.weapon = 'sword'

		# Master name
		self.name = 'Normal'
		self.direction = 'down'
		self.appearance = master1Img

	# Class Methods ---
	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def draw(self, direction):
		if self.name == 'Ghost':
			self.appearance = master2Img
		if direction == 'down':
			gameDisplay.blit(self.appearance, (self.x, self.y), (0, 0, 32, 64))
		elif direction == 'up':
			gameDisplay.blit(self.appearance, (self.x, self.y), (32, 0, 32, 64))
		elif direction == 'right':
			gameDisplay.blit(self.appearance, (self.x, self.y), (64, 0, 32, 64))
			# if self.weapon == 'sword':
			#	sword = pygame.transform.flip(sword0Img, 0, 1)
			#	gameDisplay.blit(sword, (self.x + 13, self.y + 45))
		elif direction == 'left':
			gameDisplay.blit(self.appearance, (self.x, self.y), (96, 0, 32, 96))
		#gameDisplay.blit(Mastersrc,(self.x,dispHeight-self.y))
		#pygame.draw.circle(gameDisplay, self.color,
		# [self.x, self.y], self.size )


class Monster:
	def __init__(self):
		# --- Class Attributes ---
		# Master position
		self.x = 0
		self.y = 0

		# Master's vector
		self.change_x = 0
		self.change_y = 0

		# Master name
		self.name = 'Normal'
		self.direction = 'down'
		if self.name == 'Normal':
			self.appearance = neko1Img
		if self.name == 'Ghost':
			self.appearance = neko2Img

	# --- Class Methods ---
	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def draw(self):
		gameDisplay.blit(self.appearance, (self.x, self.y))
		# gameDisplay.blit(Mastersrc,(self.x,dispHeight-self.y))
		# pygame.draw.circle(gameDisplay, self.color,
		# [self.x, self.y], self.size )

	def laser(self):
		pygame.draw.line(gameDisplay, green, [self.x + cateyeWidth, self.y +
			cateyeHeight], [self.x + cateyeWidth, 635], 1)
		pygame.draw.line(gameDisplay, green, [self.x + catWidth - cateyeWidth,
			self.y + cateyeHeight], [self.x + catWidth - cateyeWidth, 635], 1)

# introMenu()
GMaster = Master()
GMonster = Monster()
GMaster.name = "Normal"
GMaster.x = 0
GMaster.y = dispHeight - 64
masterDirection = 'right'
catmoveRight = True
pygame.mixer.music.load("music/xm/noist_transp.xm")
pygame.mixer.music.play(-1, 0)
label = myfont.render("", 1, white)
music_on = True

GMonster.x = 20
GMonster.y = 20
victorymusic = True
gamecomplete = False
justhit = False
fullscreen = False


def hitDetec(justhit):
	if not justhit:
		masterRect = pygame.Rect(GMaster.x + 4, GMaster.y, 24, 64)
		laser1Rect = (GMonster.x + cateyeWidth, GMonster.y + cateyeHeight, 1, 600)
		laser2Rect = (GMonster.x + catWidth - cateyeWidth,
		GMonster.y + cateyeHeight, 1, 600)
		if masterRect.colliderect(laser1Rect) or masterRect.colliderect(laser2Rect):
			GMaster.name = "Ghost"
			GMaster.hitpoints -= 1
			justhit = True
	return justhit


def drawSnow():
	for x in range(0, dispWidth, 256):
		for y in range(0, dispHeight, 256):
			star_x = random.randint(0, dispWidth)
			star_y = random.randint(0, dispHeight)
			pygame.draw.line(gameDisplay, white, [star_x - 3, star_y - 3],
				[star_x + 3, star_y + 3], 1)
			pygame.draw.line(gameDisplay, white, [star_x, star_y - 4],
			[star_x, star_y + 4], 1)
			pygame.draw.line(gameDisplay, white, [star_x + 3, star_y - 3],
				[star_x - 3, star_y + 3], 1)
			pygame.draw.line(gameDisplay, white, [star_x - 4, star_y],
				[star_x + 4, star_y], 1)

while (1):
	if GMaster.hitpoints <= 0:  # Game over
		GMaster.x = 0
		GMaster.y = dispHeight - 64
		GMaster.name = "Normal"
		GMaster.change_x = 0
		GMaster.change_y = 0
		GMaster.hitpoints = 3
	# gameDisplay.blit(bg0Img, [0, 0],(0,0*768,1366,768))
	else:
		if GMaster.x >= dispWidth - 24:  # Game completed
			gameDisplay.fill(black)
			drawSnow()
			victorylabel = myfont.render("Victorious", 0, blue)
			gameDisplay.blit(victorylabel, (dispWidth / 2 - 80, dispHeight / 2))
			pygame.display.update()
			gamecomplete = True
			if victorymusic:
				pygame.mixer.music.load("music/xm/nobody.xm")
				pygame.mixer.music.play(-1, 0)
				victorymusic = False
		if not gamecomplete:
			gameDisplay.fill(black)
			#pygame.draw.line(gameDisplay, white, [0, 640], [1366, 640], 6)
			gameDisplay.blit(label, (100, 660))
			drawSnow()
			healthlabel = myfont.render(str(GMaster.hitpoints) + "( )", 1, red)
			gameDisplay.blit(healthlabel, (dispWidth - 80, 30))
			gameDisplay.blit(master1Img, (dispWidth - 45, 37), (0, 0, 32, 27))
			# gameDisplay.blit(masterh, (dispWidth - 45, 33))
			#generateLevel()
			if GMonster.x < dispWidth - catWidth - 20 and catmoveRight:
				GMonster.change_x = 4
			else:
				catmoveRight = False
			if GMonster.x > 20 and not catmoveRight:
				GMonster.change_x = -4
			else:
				catmoveRight = True

			GMonster.move()
			GMonster.draw()
			if tickcount > fps / 3:
				gameDisplay.blit(neko1Img, (20, 660))
				label = myfont.render(u"吾輩は猫である。", 1, white)
				GMonster.laser()
				if not justhit:
					justhit = hitDetec(justhit)
			if tickcount > fps:
				#gameDisplay.blit(masterh, (20,660))
				justhit = False
				GMaster.name = 'Normal'
				label = myfont.render(u"お前を殺す！", 1, white)
				tickcount = 0
				GMaster.appearance = master1Img
			GMaster.move()
			GMaster.draw(masterDirection)
			# pygame.draw.rect(gameDisplay, red, (GMaster.x+4,GMaster.y,24,64), 0)
			# draw hitbox
			pygame.display.update()
			clock.tick(fps)
			tickcount += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				# if event.key == pygame.K_DOWN:
				#	GMaster.change_x=0
				#	GMaster.change_y=8
				#	masterDirection='down'
				# if event.key == pygame.K_UP:
				#	GMaster.change_x=0
				#	GMaster.change_y=-8
				#	masterDirection='up'
			elif event.type == pygame.KEYDOWN:          # check for key presses
				if event.key == pygame.K_LEFT:        # left arrow turns left
					pressed_left = True
				elif event.key == pygame.K_RIGHT:     # right arrow turns right
					pressed_right = True
				elif event.key == pygame.K_UP:        # up arrow goes up
					pressed_up = True
				elif event.key == pygame.K_DOWN:     # down arrow goes down
					pressed_down = True
			elif event.type == pygame.KEYUP:            # check for key releases
				if event.key == pygame.K_LEFT:        # left arrow turns left
					pressed_left = False
				elif event.key == pygame.K_RIGHT:     # right arrow turns right
					pressed_right = False
				elif event.key == pygame.K_UP:        # up arrow goes up
					pressed_up = False
				elif event.key == pygame.K_DOWN:     # down arrow goes down
					pressed_down = False
				elif event.key == K_SPACE:
					GMaster.x = 0
					GMaster.y = 574
					GMaster.name = "Normal"
					GMaster.change_x = 0
					GMaster.change_y = 0
					GMaster.hitpoints = 3
				#elif event.key == K_RETURN:
				elif event.key == K_m:
					if music_on:
						pygame.mixer.music.pause()
						music_on = False
					else:
						pygame.mixer.music.unpause()
						music_on = True
				elif event.key == K_ESCAPE:
					pygame.quit()
					quit()
				elif event.key == K_f:
					if not fullscreen:
						gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
							pygame.FULLSCREEN)
						fullscreen = True
					else:
						gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))
						fullscreen = False
		if pressed_left:
			GMaster.change_x = -8
			masterDirection = 'left'
		if pressed_right:
			GMaster.change_x = 8
			masterDirection = 'right'
		#if pressed_up:
		#	GMaster.change_y=-4
		#if pressed_down:
		#	GMaster.change_y=4

