import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from button import Button

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
		self.start_button = Button(screen_width//2 - self.start_img.get_width()//2, 200, self.start_img)
		self.exit_button = Button(screen_width//2 - self.exit_img.get_width()//2, 400, self.exit_img)
		pygame.display.set_caption("2D Platformer Game")

	def run(self):

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			background = pygame.image.load(path.join(base_path, 'bg.png')).convert()
			background = pygame.transform.smoothscale(background, self.screen.get_size())
			self.screen.blit(background, (0, 0))
	
			if not self.main_menu:
				self.level.run()
			if not self.level.check_player():
				return 1
				#self.main_menu = True
				pass
			if self.main_menu == True:
				self.start_button.draw(self.screen)
				self.exit_button.draw(self.screen)

			if self.start_button.clicked:
				self.main_menu = False

			if self.exit_button.clicked:
				#pygame.quit()
				#sys.exit()
				return 2

			pygame.display.update()
			self.clock.tick(clock_tick)

if __name__ == '__main__':
	main = Main()
	while main.run() != 2:
		main = Main()
		main.run
