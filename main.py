import pygame
from particle import Particle
from random import randint
from rocket import Rocket

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fireworks")

black = (0, 0, 0)
white = (255, 255, 255)
fps = pygame.time.Clock()
FPS = 60

particles = []
rockets = []

def explode(x, y, color):
	mouse = pygame.mouse.get_pos()
	for i in range(50):
		particles.append(Particle(x, y, color))

def close():
	pygame.quit()
	quit()

def render():
	window.fill(black)
	
	for p in particles:
		p.show(window)
		p.update()
		
	for r in rockets:
		r.show(window)
		r.update()
		if r.v <= 0:
			explode(r.x, r.y, r.color)
			rockets.remove(r)
		
	#if randint(0, 100) <= 10:
	#	explode(randint(0, width), randint(0, height), (randint(0, 255), randint(0, 255), randint(0, 255)))	
	
	if randint(0, 100) <= 5:
		rockets.append(Rocket((randint(0, 255), randint(0, 255), randint(0, 255))))
	
	
	pygame.display.update()
	fps.tick(FPS)
	
def loop():
	while True:
		render()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				close()
				
loop()
