import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from button import Button
from os import path

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
main_menu = True
start_img = pygame.image.load(path.join(base_path , 'buttons', 'start-1.png')).convert_alpha()
exit_img= pygame.image.load(path.join(base_path, 'buttons','exit-1.png')).convert_alpha()
start_button = Button(screen_width//2 - start_img.get_width()//2, 200, start_img)
exit_button = Button(screen_width//2 - exit_img.get_width()//2, 400, exit_img)
pygame.display.set_caption("2D Platformer Game")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	background = pygame.image.load(path.join(base_path, 'bg.png')).convert()
	background = pygame.transform.smoothscale(background, screen.get_size())
	screen.blit(background, (0, 0))

	if start_button.clicked:
		main_menu = False

	if exit_button.clicked:
		pygame.quit()
		sys.exit()

	if main_menu == True:
		start_button.draw(screen)
		exit_button.draw(screen)
	else:
		level.run()


	pygame.display.update()
	clock.tick(clock_tick)
