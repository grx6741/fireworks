import pygame
from random import randint
from pygame.math import Vector2

class Rocket:
	def __init__(self, color):
		self.x = randint(0, 800)
		self.v = randint(10, 20)
		self.y = 600
		self.acc = -0.5
		self.color = color
		
	def show(self, window):
		pygame.draw.circle(window, self.color, (self.x, self.y), 5)
		
	def update(self):
		self.y -= self.v
		self.v += self.acc 
