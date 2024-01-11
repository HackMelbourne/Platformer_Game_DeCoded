import pygame
from settings import tile_types

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, tile_type):
        super().__init__()
        self.image = pygame.Surface((size, size))
        sprite_surface = pygame.image.load(tile_types[tile_type])
        sprite_surface = pygame.transform.smoothscale(sprite_surface, (size, size))
        self.image.blit(sprite_surface, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
