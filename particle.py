import pygame
from pygame.math import Vector2
from random import randint

class Particle:
	def __init__(self, x, y, color):
		self.pos = Vector2(x, y)
		self.vel = Vector2(randint(-10, 10), randint(-15, 10))
		self.acc = Vector2(0, 0.5)
		self.size = 10
		self.color = color
		
	def show(self, window):
		pygame.draw.circle(window, self.color, (self.pos.x, self.pos.y), self.size)
		
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
		self.size -= 0.5
