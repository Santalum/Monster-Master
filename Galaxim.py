#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division
import pygame
#import sys
import time
import math
import random
from pygame.locals import *
#particle
particle0Img = pygame.image.load('sprite/particle/0anim.png')


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)

pygame.init()
pygame.display.set_caption("Galaxim")
dispWidth = 800  # 1366  # 800  # 1366
dispHeight = 600  # 768  # 600  # 768
gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))
pygame.mixer.music.load("music/xm/noist_transp.xm")
pygame.mixer.music.play(-1, 0)


clock = pygame.time.Clock()
fps = 60
bounce = False
fullscreen = False
music_on = True


def inpCtrl():
	global fullscreen
	global music_on
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:
				GParticle.x = dispWidth // 2
				GParticle.y = dispHeight // 2
				GParticle.change_y = 0
				GParticle.change_x = 0
			elif event.key == K_f:
				if not fullscreen:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),
						pygame.FULLSCREEN)
					fullscreen = True
				else:
					gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))
					fullscreen = False
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


GParticle = Particle()

while (1):
	gameDisplay.fill([0, 0, 0])
	drawSnow()
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
	if bounce:
		GParticle.change_y -= 1
		#GParticle.change_x += 1
	else:
		GParticle.change_y += 1
		#GParticle.change_x -= 1
	GParticle.moveangular()
	#pygame.draw.ellipse(gameDisplay, green,
		#(dispWidth // 2 - 64, dispHeight // 2 - 32, 128, 64), 1)
	#GParticle.move()
	if GParticle.y >= dispHeight // 2 + 64:
		bounce = True
		GParticle.change_y = 0
		GParticle.change_x = 0
	elif GParticle.y <= dispHeight // 2 - 64:
		bounce = False
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
	pygame.display.update()
	clock.tick(fps)
	inpCtrl()
