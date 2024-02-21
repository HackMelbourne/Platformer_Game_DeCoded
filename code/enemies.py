import pygame
from os import path
from settings import base_path, import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos) -> None:
        super().__init__()
        self.import_character_assets((32,64))
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.Vector2(1,0)
        self.speed = 1
        self.animation_speed = 0.25
        self.status = 'idle'
        self.gravity = 0.8
        self.on_ground = False
        self.on_left = False
        self.on_right = False
        self.facing = 'right'

    def import_character_assets(self,size:(int,int)):
        character_path = path.join(base_path, 'enemy')
        animation_file_counts = {
            'idle': 5,
            'run': 7,
        }
        self.animations = {'idle': [], 'run': []}

        for animation in self.animations.keys():
            full_path = path.join(character_path, animation)
            self.animations[animation] = [
                pygame.transform.smoothscale(
                    pygame.image.load(f'{path.join(full_path,str(i))}.png').convert_alpha(),
                    size)
                for i in range(animation_file_counts[animation])]

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        self.frame_index %= len(animation)
        img = pygame.transform.scale(animation[int(self.frame_index)], (32, 64)).convert_alpha()
        if self.direction.x < 0:
            self.image = pygame.transform.flip(img, True, False).convert_alpha()
            self.facing = 'left'
        else:
            self.image = img.convert_alpha()
            self.facing= 'right'

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False).convert_alpha()
        self.direction.x *= -1
        if self.direction.x < 0:
            self.facing = 'left'
        else:
            self.facing = 'right'
    def get_status(self):
        if self.direction.x == 0:
            self.status = 'idle'
        else:
            self.status = 'run'

    def move(self):
        self.rect.x += self.direction.x * self.speed

    def update(self, shift) -> None:
        self.get_status()
        self.rect.x += shift
        self.animate()
