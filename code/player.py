import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
 
        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -14

        # Jumping and ground state
        self.jump_count = 0
        self.on_ground = False
        self.max_jumps = 2

        self.jumping = False
        self.jump_key_pressed = False  # Track if jump key is still pressed

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            if not self.jump_key_pressed:
                self.jump()
                self.jump_key_pressed = True
        else:
            self.jump_key_pressed = False


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        if self.on_ground:
            self.jump_count = 0

    def jump(self):
        if self.jump_count < self.max_jumps:
            self.direction.y = self.jump_speed
            self.on_ground = False
            self.jump_count += 1


    def update(self):
        self.get_input()
