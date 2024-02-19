import pygame
from settings import base_path

class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        sprite = pygame.image.load(base_path, 'Tiles', 'window.png')
        sprite_surface = pygame.transform.smoothscale(sprite, (32, 64)).convert_alpha()
        sprite_surface.set_colorkey((0, 0, 0))
        self.image.blit(sprite_surface, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
