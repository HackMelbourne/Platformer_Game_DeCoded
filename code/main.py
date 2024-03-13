import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from button import Button
from os import path

class Main:

# Pygame setup
	def __init__(self) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((screen_width,screen_height))
		self.clock = pygame.time.Clock()
		self.level = Level(level_map, self.screen)
		self.main_menu = True
		self.start_img = pygame.image.load(base_path + '\\buttons\\start-1.png').convert_alpha()
		self.exit_img= pygame.image.load(base_path + '\\buttons\\exit-1.png').convert_alpha()
		self.menu_img = pygame.image.load(path.join(base_path, 'title.png')).convert_alpha()

		self.start_button = Button(screen_width//2 - self.start_img.get_width()//2, 500, self.start_img)
		self.exit_button = Button(screen_width//2 - self.exit_img.get_width()//2, 600, self.exit_img)
		pygame.display.set_caption("2D Platformer Game")


	def run(self):
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
			# Check if the game is in the main menu state
			if self.main_menu:
				# Load the main menu background image
				background_img = pygame.image.load(path.join(base_path, 'sky1.png')).convert()
			else:
				# Load the level background image
				background_img = pygame.image.load(path.join(base_path, 'bg.png')).convert()

			# Resize the background image to match the screen size
			background_img = pygame.transform.smoothscale(background_img, self.screen.get_size())

			# Blit the background image onto the screen
			self.screen.blit(background_img, (0, 0))

			# Handle game logic based on the current state
			if not self.main_menu:
				self.level.run()
			if not self.level.check_player():
				return 1

			if self.main_menu == True:
				# Draw the main menu buttons
				self.screen.blit(self.menu_img, (screen_width//2 - self.menu_img.get_width()//2, 50))
				self.start_button.draw(self.screen)
				self.exit_button.draw(self.screen)

			if self.start_button.clicked:
				self.main_menu = False

			if self.exit_button.clicked:
				return 2

			pygame.display.update()
			self.clock.tick(clock_tick)

if __name__ == '__main__':
	main = Main()
	while main.run() != 2:
		main = Main()
		main.run()
