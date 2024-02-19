import pygame
from settings import base_path
from os import path

class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        sprite = pygame.image.load(path.join(base_path, 'Tiles\window.png'))
        sprite_surface = pygame.transform.smoothscale(sprite, (32, 64)).convert_alpha()
        sprite_surface.set_colorkey((0, 0, 0))
        self.image = sprite_surface
        
        self.image.blit(sprite_surface, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
