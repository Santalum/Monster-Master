#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division
import pygame
import math
#import sys
import time
import random
from pygame.locals import *

random.seed()
pygame.init()
pygame.display.set_caption("Monster Master")
myfont = pygame.font.SysFont("TakaoMincho", 40)
myfont2 = pygame.font.SysFont("helvet", 16)
myfont3 = pygame.font.SysFont("TakaoMincho", 24)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
lightred = (127, 0, 0)
green = (0, 255, 0)
lightgreen = (0, 127, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 127)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
darkyellow = (127, 127, 0)
saddlebrown = (139, 69, 19)
sienna = (160, 82, 45)
bg = black
masterHealth = 3
cateyeHeight = 16
cateyeWidth = 18
catWidth = 64
catHeight = 48

levelcount = 1

catmoveRight = True
music_on = False
victorymusic = True
gamecomplete = False
justhit = False
fullscreen = False
intro = True
mainmusic = True
music_changed = False

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
master_x = dispWidth // 2 - 96
master_y = dispHeight - 64
master_direction = 0
show_inventory = False
tickcount = 0
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))
iconImg = pygame.image.load("icon32.png")
pygame.display.set_icon(iconImg)
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
floor0Img = pygame.image.load('sprite/floor/0.png')
floor1Img = pygame.image.load('sprite/floor/1.png')
floor0sImg = pygame.image.load('sprite/floor/0s.png')
orb = pygame.image.load('sprite/item/orb.png')
#NPC DE ARU
npc1Img = pygame.image.load('sprite/npc/npc1.png')
#nekodearu
neko1Img = pygame.image.load('sprite/cat/neko1.png')
neko2Img = pygame.image.load('sprite/cat/neko2.png')
#particle
particle0Img = pygame.image.load('sprite/particle/0anim.png')


def text_objects(text, font):
	textSurface = font.render(text, True, green)
	return textSurface, textSurface.get_rect()


def introMenu():
	if music_on:
		#pygame.mixer.music.load("music/xm/WoA.xm")
		pygame.mixer.music.load("music/xm/WoA.xm")
		pygame.mixer.music.play(-1, 0)
	intro_screen('Static Studio', 2, 0)
	intro_screen('Proudly Presents', 2, 1)
	intro_screen('Monster Master', 2, 2)
	#masterMove = distance / (13*fps)
	#menu_screen((dispHeight / 2) / (13 * fps))	 # 0.34871794871)
	if intro:
		for y in range(0, 2 * fps):
			gameDisplay.fill(black)
			drawSnow()
			drawPlanet()
			#gameDisplay.blit(bg1Img, [0, 0], (0, 3 * 768, 1366, 768))
			master(master_x, -64 + 13 * y * ((dispHeight / 4) / (13 * fps)), 2)
			pygame.display.update()
			clock.tick(fps)
			inpCtrl()
			if not intro:
				break
		if music_on:
		#pygame.mixer.music.load("music/xm/WoA.xm")
			pygame.mixer.music.load("music/midi/nobody's area_46 midi_cut.mid")
			pygame.mixer.music.play(-1, 0)
		gameDisplay.blit(bg0Img, [0, 0], (0, 3 * 768, 1366, 768))
		master(master_x, master_y, 0)
		pygame.display.update()
		#time.sleep(0.2)
		drawMenu()

menudisplay = True


def drawMenu():
	global menudisplay
	GMaster.y = dispHeight // 2 - 64
	GMaster.x = dispWidth // 2 - 96
	while menudisplay:
		menuCtrl()
		clock.tick(fps)
		#bgImgDsp = bg4Img.subsurface(0, 0, 640, 480)
		#bgImgDsp = pygame.transform.scale(bgImgDsp,
		#	(dispWidth, dispHeight))
		#gameDisplay.blit(bgImgDsp, [0, 0], (0, 0, 1366, 768))
		gameDisplay.fill(black)
		drawSnow()
		drawPlanet()
		GMaster.draw()
		largeText = pygame.font.Font('freesansbold.ttf', (dispWidth // 18))
		TextSurf, TextRect = text_objects("Play", largeText)
		TextRect.center = ((dispWidth // 2), (dispHeight // 2 - 48))
		gameDisplay.blit(TextSurf, TextRect)
		largeText = pygame.font.Font('freesansbold.ttf', (dispWidth // 18))
		TextSurf, TextRect = text_objects("Exit", largeText)
		TextRect.center = ((dispWidth // 2), (dispHeight // 2 + 48))
		gameDisplay.blit(TextSurf, TextRect)
		pygame.display.update()

# actually here should be a timer after which a demo display can be created


def intro_screen(text, showTime, ndx):
	if intro:
		largeText = pygame.font.Font('freesansbold.ttf', (dispWidth // 10))
		TextSurf, TextRect = text_objects(text, largeText)
		TextRect.center = ((dispWidth // 2), (dispHeight // 2))
		gameDisplay.fill(black)
		bgImgDsp = bg0Img.subsurface(0, ndx * 768, 1366, 768)
		bgImgDsp = pygame.transform.scale(bgImgDsp,
			(dispWidth, dispHeight))
		#gameDisplay.blit(bg0Img, [0, 0], (0, ndx * 768, 1366, 768))
		gameDisplay.blit(bgImgDsp, [0, 0], (0, 0, 1366, 768))
		gameDisplay.blit(TextSurf, TextRect)
		pygame.display.update()
		for x in range(0, showTime * fps):
			inpCtrl()
			clock.tick(fps)
			if not intro:
				break


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
	global levelcount
	global music_changed
	if levelcount == 0:
		levelcount == 2
	if levelcount == 3:
		levelcount = 1
	if levelcount == 1:
		gameDisplay.fill(white)
		for x in range(0, dispWidth // 64 + 1):
			for y in range(0, dispHeight // 64 + 1):
				gameDisplay.blit(floor0sImg, (x * 64, y * 64))
		if not music_changed:
			if music_on:
				#pygame.mixer.music.load("music/xm/noist_transp.xm")
				pygame.mixer.music.load("music/midi/Number Two_9 midi.mid")
				pygame.mixer.music.play(-1, 0)
			music_changed = True
	if levelcount == 2:
		gameDisplay.fill(white)
		for x in range(0, dispWidth // 128 + 1):
			for y in range(0, dispHeight // 128 + 1):
				gameDisplay.blit(floor1Img, (x * 128, y * 128))
		if not music_changed:
			if music_on:
				#pygame.mixer.music.load("music/xm/nobody.xm")
				pygame.mixer.music.load("music/midi/Number Three_11 midi.mid")
				pygame.mixer.music.play(-1, 0)
			music_changed = True


	# pygame.display.update ()


class Particle:
	def __init__(self):
		self.x = dispWidth // 2 - 16 - 60
		self.y = dispHeight // 2 - 12
		self.change_x = 0
		self.change_y = 0
		self.appearance = particle0Img
		# initial frame index
		self.index = 0
		# initial angle of movement
		self.angle = 0
		self.rangle = 0
		self.speed = 1
		self.size = 0.75

	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def moveangular(self):
		self.x += math.sin(self.rangle) * self.speed
		self.y -= math.cos(self.rangle) * self.speed * 0.2

	def draw(self):
		# gameDisplay.blit(self.appearance, (self.x, self.y))
		ballsprite = self.appearance.subsurface(0, self.index * 32, 32, 32)
		ballsprite = pygame.transform.rotate(ballsprite, self.angle)
		ballsprite = pygame.transform.scale(ballsprite,
			(int(self.size * 32), int(self.size * 32)))
		gameDisplay.blit(ballsprite, (self.x, self.y))


class Master:
	def __init__(self):
		# Class Attributes ---
		# Master position
		self.x = 0
		self.y = 0
		# HP, MP, XP, level
		self.hitpoints = 3
		self.maxhp = 3
		self.manapoints = 16
		self.maxmp = 16
		self.experiencepoints = 0
		self.maxxp = 100
		self.level = 1
		self.maxlv = 2
		# Master's vector
		self.change_x = 0
		self.change_y = 0
		self.weapon = 'sword'
		# Master name
		self.name = 'Normal'
		self.direction = 'right'
		self.appearance = master1Img

	# Class Methods ---
	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def draw(self):
		if self.name == 'Ghost':
			self.appearance = master2Img
		if self.direction == 'down':
			gameDisplay.blit(self.appearance, (self.x, self.y), (0, 0, 32, 64))
		elif self.direction == 'up':
			gameDisplay.blit(self.appearance, (self.x, self.y), (32, 0, 32, 64))
		elif self.direction == 'right':
			gameDisplay.blit(self.appearance, (self.x, self.y), (64, 0, 32, 64))
			# if self.weapon == 'sword':
			#	sword = pygame.transform.flip(sword0Img, 0, 1)
			#	gameDisplay.blit(sword, (self.x + 13, self.y + 45))
		elif self.direction == 'left':
			gameDisplay.blit(self.appearance, (self.x, self.y), (96, 0, 32, 96))
		#gameDisplay.blit(Mastersrc,(self.x,dispHeight-self.y))
		#pygame.draw.circle(gameDisplay, self.color,
		# [self.x, self.y], self.size )


class NPC:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.appearance = npc1Img
		self.dialogue = ["Hello!", "Nice to meet you.", "What is your name?", "Hendrik.","", "Hello!", ""]#("Hello","Hi")]
		self.response = ["Hello!", "Nice to meet you too.", "My name is Stefan, what is yours?", "Alright see you around!", "","Hi!", ""]

	def draw(self):
		gameDisplay.blit(self.appearance, (self.x, self.y), (0, 0, 32, 64))


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

GParticle = Particle()


def drawPlanet():
	pygame.draw.arc(gameDisplay, green,
		(dispWidth // 2 - 96, dispHeight // 2 - 16, 192, 32), 0, math.pi, 4)
	# move particle in front of circle
	if (GParticle.rangle / math.pi) % 2 >= 1:
		pygame.draw.circle(gameDisplay, red, (dispWidth // 2, dispHeight // 2), 32, 0)
	# particle time
	GParticle.draw()
	# move particle behind circle
	if (GParticle.rangle / math.pi) % 2 < 1:
		pygame.draw.circle(gameDisplay, red, (dispWidth // 2, dispHeight // 2), 32, 0)
	pygame.draw.arc(gameDisplay, green,
		(dispWidth // 2 - 96, dispHeight // 2 - 16, 196, 32), math.pi, 2 * math.pi, 4)
	#GParticle.change_x = (GParticle.index - 4) * 2
	#if bounce:
		#GParticle.change_y -= 1
		##GParticle.change_x += 1
	#else:
		#GParticle.change_y += 1
		##GParticle.change_x -= 1
	GParticle.moveangular()
	#pygame.draw.ellipse(gameDisplay, green,
		#(dispWidth // 2 - 64, dispHeight // 2 - 32, 128, 64), 1)
	#GParticle.move()
	if GParticle.y >= dispHeight // 2 + 64:
		#bounce = True
		GParticle.change_y = 0
		GParticle.change_x = 0
	elif GParticle.y <= dispHeight // 2 - 64:
		#bounce = False
		#GParticle.change_y = 0
		GParticle.change_x = 0
	#elif GParticle >= dispHeight // 2:
		#GParticle.change_y += 2
	if GParticle.index < 9:
		GParticle.index += 1
		#GParticle.x += 8
	else:
		GParticle.index = 0
		GParticle.angle += 10
		GParticle.rangle += math.pi / 2 / 9
		GParticle.size = 3 / 4 - 1 / 4 * math.sin(GParticle.rangle)
		#print(GParticle.rangle, GParticle.size, math.sin(GParticle.rangle))

NPC1 = NPC()
NPC1.x = dispWidth // 2
NPC1.y = dispHeight // 2
GMaster = Master()
GMonster = Monster()
GMaster.name = "Normal"
GMaster.x = dispWidth // 2
GMaster.y = dispHeight - 64
masterDirection = 'right'
label = myfont.render("", 1, white)
GMonster.x = 20
GMonster.y = 20
GMaster.speed = 4


def wallColl():
	# original values dW/24 and dH/19
	x = GMaster.x // (dispWidth // 12) + GMaster.change_x // GMaster.speed + 1
	y = GMaster.y // (dispHeight // 9) + GMaster.change_y // GMaster.speed + 1
	#print x, y
	#print  GMaster.change_x // GMaster.speed, GMaster.change_y // GMaster.speed
	#print len(level)
	#print len(level[y])
	if level[y][x] == 'W':
		GMaster.change_x = 0
		GMaster.change_y = 0
		#print level[y][x]
		return True
	#if level[x + deltaX, y + deltaY] == 'W':
		#return True
	#else:
		#return False


def menuCtrl():
	global fullscreen
	global music_on
	global pressed_right
	global pressed_left
	global pressed_up
	global pressed_down
	global intro
	global menudisplay
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
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
			#elif event.key == K_SPACE:
				#spawnMaster()
			elif event.key == K_RETURN:
				if GMaster.y == dispHeight // 2 - 64:
					menudisplay = False
				if GMaster.y == dispHeight // 2 + 32:
					pygame.quit()
					quit()
			elif event.key == K_m:
				if music_on:
					pygame.mixer.music.pause()
					music_on = False
				else:
					pygame.mixer.music.unpause()
					music_on = True
			elif event.key == K_ESCAPE:
				if intro:
					intro = False
				elif not intro:
					pygame.quit()
					quit()
			elif event.key == K_f:
				if not fullscreen:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
						pygame.FULLSCREEN)
					fullscreen = True
				else:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))  # lint:ok
					fullscreen = False
	if pressed_up:
		GMaster.y = dispHeight // 2 - 64
		GMaster.direction = 'right'
		#else:
		#	GMaster.y = 0
	if not pressed_up or pressed_down:
		GMaster.change_y = 0
	if pressed_down:
		GMaster.y = dispHeight // 2 + 32
		GMaster.direction = 'right'
		#else:
		#	GMaster.y = dispHeight - 64

pressed_z = False


def inpCtrl():
	global fullscreen
	global music_on
	global pressed_right
	global pressed_left
	global pressed_up
	global pressed_down
	global pressed_z
	global intro
	global menudisplay
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
			elif event.key == pygame.K_z:
				pressed_z = False
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
				spawnMaster()
			#elif event.key == K_RETURN:
			elif event.key == K_m:
				if music_on:
					pygame.mixer.music.pause()
					music_on = False
				else:
					pygame.mixer.music.unpause()
					music_on = True
			elif event.key == K_z:
				pressed_z = True
			elif event.key == K_ESCAPE:
				if intro:
					intro = False
				elif not intro:
					menudisplay = True
					drawMenu()
					#pygame.quit()
					#quit()
			elif event.key == K_f:
				if not fullscreen:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
						pygame.FULLSCREEN)
					fullscreen = True
				else:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))  # lint:ok
					fullscreen = False
	if pressed_left:
		GMaster.change_x = -4
		GMaster.direction = 'left'
	if not pressed_left or pressed_right:
		GMaster.change_x = 0
	if pressed_right:
			GMaster.change_x = 4
			GMaster.direction = 'right'
	if pressed_up:
		#if GMaster.y > 0:
			GMaster.change_y = -4
			GMaster.direction = 'up'
		#else:
		#	GMaster.y = 0
	if not pressed_up or pressed_down:
		GMaster.change_y = 0
	if pressed_down:
		#if GMaster.y < dispHeight - 64:
			GMaster.change_y = 4
			GMaster.direction = 'down'
		#else:
		#	GMaster.y = dispHeight - 64


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


# wagahai wa yuki de aru
def drawSnow():
	for x in range(0, dispWidth, 256):
		for y in range(0, dispHeight, 256):
			star_colour_i = random.randint(0, 6)
			if star_colour_i == 0:
				star_colour = white
			elif star_colour_i == 1:
				star_colour = red
			elif star_colour_i == 2:
				star_colour = green
			elif star_colour_i == 3:
				star_colour = blue
			elif star_colour_i == 4:
				star_colour = cyan
			elif star_colour_i == 5:
				star_colour = magenta
			elif star_colour_i == 6:
				star_colour = yellow
			star_x = random.randint(0, dispWidth)
			star_y = random.randint(0, dispHeight)
			pygame.draw.line(gameDisplay, star_colour, [star_x - 3, star_y - 3],
				[star_x + 3, star_y + 3], 1)
			pygame.draw.line(gameDisplay, star_colour, [star_x, star_y - 4],
			[star_x, star_y + 4], 1)
			pygame.draw.line(gameDisplay, star_colour, [star_x + 3, star_y - 3],
				[star_x - 3, star_y + 3], 1)
			pygame.draw.line(gameDisplay, star_colour, [star_x - 4, star_y],
				[star_x + 4, star_y], 1)


def drawHUD():
	pygame.draw.rect(gameDisplay, black,
		(8, 16, 20, 64))
	#pygame.draw.rect(gameDisplay, black,
	#	(dispWidth // 24, dispHeight // 32 + 48,
	#	64, 16))
	hplabel = myfont2.render("HP", 1, red)
	gameDisplay.blit(hplabel, (dispWidth // 32 - 16, dispHeight // 32))
	mplabel = myfont2.render("MP", 1, blue)
	gameDisplay.blit(mplabel, (dispWidth // 32 - 16, dispHeight // 32 + 16))
	xplabel = myfont2.render("XP", 1, yellow)
	gameDisplay.blit(xplabel, (dispWidth // 32 - 16, dispHeight // 32 + 32))
	lvlabel = myfont2.render("LV   " + str(GMaster.level), 1, green)
	gameDisplay.blit(lvlabel, (dispWidth // 32 - 16, dispHeight // 32 + 48))
	pygame.draw.rect(gameDisplay, lightred,
		(dispWidth // 24, dispHeight // 32, 64, 16))
	pygame.draw.rect(gameDisplay, red,
		(dispWidth // 24, dispHeight // 32,
		GMaster.hitpoints * 64 // GMaster.maxhp, 16))
	pygame.draw.rect(gameDisplay, darkblue,
		(dispWidth // 24, dispHeight // 32 + 16, 64, 16))
	pygame.draw.rect(gameDisplay, blue,
		(dispWidth // 24, dispHeight // 32 + 16,
		GMaster.manapoints * 64 // GMaster.maxmp, 16))
	pygame.draw.rect(gameDisplay, darkyellow,
		(dispWidth // 24, dispHeight // 32 + 32, 64, 16))
	pygame.draw.rect(gameDisplay, yellow,
		(dispWidth // 24, dispHeight // 32 + 32,
		GMaster.experiencepoints * 64 // GMaster.maxxp, 16))


class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
		gameDisplay.blit(wall0Img, [pos[0], pos[1]],(pos[0], pos[1], 32, 32))


walls = []  # List to hold the walls


def drawWalls(levelcount):
	global level
	# Holds the level layout in a list of strings.
	if levelcount == 1:
		level = [
		"WWWWWWWWWWWWWWWWWWWWWWWWW",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                        ",
		"W                       ",
		"W                       ",
		"W                       W",
		"W                       W",
		"W                       W",
		"W                       W",
		"WWWWWWWWWWWWWWWWWWWWWWWWW",
		]
		NPC1.draw()
	if levelcount == 2:
				level = [
		"WWWWWWWWWWWWWWWWWWWWWWWWW",
		"W          w  W   W  W  W",
		"W                    W  W",
		"W   WWWW    w  W WW  W  W",
		"W   W        WWWWWWW W  W",
		"W      WWWW  WW    W W  W",
		"W   W     WW wW    W W  W",
		"W   W     W wW  WWWW W  W",
		"W       WWWW W  W WW W  W",
		"W         WW W  W WW W  W",
		"W     W           WW W  W",
		"         WWWW W      W  W",
		"      W    WW       W   W",
		"      W    WW       W   W",
		"W     W    WW           W",
		"W     W     WW          W",
		"W     W     WW          W",
		"W     W     WW          W",
		"WWWWWWWWWWWWWWWWWWWWWWWWW",
		]
	# Parse the level string above. W = wall
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				Wall((x, y))
				gameDisplay.blit(wall0Img, (x, y))
				#pygame.draw.rect(gameDisplay, (255, 255, 255), Wall((x, y)))
			x += 32
		y += 32
		x = 0


def detectPresence(master, npc):
	if master.x -16 <= npc.x + 16 and master.x + 16 >= npc.x - 16 and master.y - 16 <= npc.y + 16 and master.y + 16 >= npc.y - 16:
		return True
	else:
		return False


def spawnMaster():
	GMaster.x = dispWidth // 2
	GMaster.y = dispHeight - 64
	GMaster.name = "Normal"
	GMaster.change_x = 0
	GMaster.change_y = 0
	GMaster.hitpoints = 3


def drawDialogue(NPC, stage):
	#if stage == 0:
		#print "lol"
	dialoguelabel = myfont3.render(NPC.dialogue[stage], 0, red)
	gameDisplay.blit(dialoguelabel, (NPC.x - dialoguelabel.get_rect().width // 2 + 16, NPC.y - 32))
	dialoguelabel = myfont3.render(NPC.response[stage], 0, green)
	gameDisplay.blit(dialoguelabel, (GMaster.x - dialoguelabel.get_rect().width // 2 + 16, GMaster.y - 32))
	#if stage == 1:
		#dialoguelabel = myfont3.render("Hello", 0, red)
		#gameDisplay.blit(dialoguelabel, (NPC.x - 16, NPC.y - 32))
		#dialoguelabel = myfont3.render("Hi", 0, green)
		#gameDisplay.blit(dialoguelabel, (GMaster.x, GMaster.y - 32))
	#if stage == 2:
		#dialoguelabel = myfont3.render("Nice to meet you I am Frank, what is your name?", 0, red)
		#gameDisplay.blit(dialoguelabel, (NPC.x - 16, NPC.y - 32))
		#dialoguelabel = myfont3.render("My memory's gone, who am I?", 0, green)
		#gameDisplay.blit(dialoguelabel, (GMaster.x, GMaster.y - 32))


NPC1dialoguestage = 0


while (1):
	GMaster.name = "Normal"
	if intro:
		introMenu()
		intro = False
	if GMaster.hitpoints <= 0:  # Game over
		spawnMaster()
	# gameDisplay.blit(bg0Img, [0, 0],(0,0*768,1366,768))
	else:
		if GMaster.x <= 0:  # level completed
			GMaster.x = 0
			#spawnMaster()
			if levelcount > 1:
				GMaster.x = dispWidth - 26
				music_changed = False
				levelcount -= 1
		if GMaster.x >= dispWidth - 24:  # level completed
			GMaster.x = dispWidth - 24
			#spawnMaster()
			if levelcount < 2:
				music_changed = False
				GMaster.x = 1
				GMaster.experiencepoints += 3
				levelcount += 1
			#gameDisplay.fill(black)
			#drawSnow()
			#drawPlanet()
			#victorylabel = myfont.render("Victorious", 0, green)
			#gameDisplay.blit(victorylabel, (dispWidth // 2 - 96, dispHeight / 2 + 16))
			#pygame.display.update()
			#gamecomplete = True
			#if victorymusic:
				#pygame.mixer.music.load("music/xm/nobody.xm")
				#pygame.mixer.music.play(-1, 0)
				#victorymusic = False
		if not gamecomplete:
			gameDisplay.fill(black)
			#if music_on:
				#if not mainmusic:
					#pygame.mixer.music.load("music/xm/oval.xm")
					#pygame.mixer.music.play(-1, 0)
					#mainmusic = True
			#pygame.draw.line(gameDisplay, white, [0, 640], [1366, 640], 6)
			#drawPlanet()
			generateLevel()
			drawSnow()
			drawWalls(levelcount)
			if pressed_z:
				if detectPresence(GMaster, NPC1):
					pressed_z = False
					if len(NPC1.dialogue) > NPC1dialoguestage +1:
						NPC1dialoguestage += 1
					else:
						NPC1dialoguestage -= 1
			if detectPresence(GMaster, NPC1):
				drawDialogue(NPC1, NPC1dialoguestage)
			#wallColl()
			drawHUD()
			#healthlabel = myfont.render(str(GMaster.hitpoints) + "( )", 1, red)
			#gameDisplay.blit(healthlabel, (dispWidth - 80, 30))
			#gameDisplay.blit(master1Img, (dispWidth - 45, 37), (0, 0, 32, 27))

			# gameDisplay.blit(masterh, (dispWidth - 45, 33))
			#if GMonster.x < dispWidth - catWidth - 20 and catmoveRight:
				#GMonster.change_x = 4
			#else:
				#catmoveRight = False
			#if GMonster.x > 20 and not catmoveRight:
				#GMonster.change_x = -4
			#else:
				#catmoveRight = True

#draw monster
			#GMonster.move()
			#GMonster.draw()
			#if tickcount > fps / 3:
				#gameDisplay.blit(neko1Img, (20, 660))
				#label = myfont.render(u"吾輩は猫である。", 1, white)
				#GMonster.laser()
				#if not justhit:
					#justhit = hitDetec(justhit)
			#if tickcount > fps:
				##gameDisplay.blit(masterh, (20,660))
				#justhit = False
				#GMaster.name = 'Normal'
				#label = myfont.render(u"お前を殺す！", 1, white)
				#tickcount = 0
				#GMaster.appearance = master1Img
			GMaster.move()
			GMaster.draw()
			# particle time
			# pygame.draw.rect(gameDisplay, red, (GMaster.x+4,GMaster.y,24,64), 0)
			# draw hitbox
			pygame.display.update()
	clock.tick(fps)
	tickcount += 1
	inpCtrl()

