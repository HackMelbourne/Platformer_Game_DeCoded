import pygame, sys
from settings import *
from tiles import Tile
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.display.set_caption("2D Platformer Game")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	background = pygame.image.load(base + 'bg.png').convert()
	background = pygame.transform.smoothscale(background, screen.get_size())
	screen.blit(background, (0, 0))
	level.run()

	pygame.display.update()
	clock.tick(60)
