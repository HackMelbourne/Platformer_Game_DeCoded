import pygame
from os import path
from settings import base_path

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.CHARACTER_WIDTH = 50
        # self.CHARACTER_HEIGHT = 60
        # self.import_character_assets((self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT))

        # Player animation state
        # self.state = 'idle'
        # self.facing_right = True
        # self.frame_index = 0
        # self.animation_speed = 0.30
        # self.image = self.animations['idle'][self.frame_index]
        # self.rect = self.image.get_rect(topleft=pos)

        # Player appearance
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # # Player attributes
        # self.max_health = 6
        # self.current_health = self.max_health

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

        # self.is_attacking = False
        # self.is_invincible = False
        # self.is_invincible_timer = 0
        # self.attacked_time = 0
        # self.attacked_dir = 0
        # self.attacked_c = 0


    # def import_character_assets(self,size:(int,int)):
    #     character_path = path.join(base_path, 'freeknight')
    #     self.animations = {'idle': [], 'run': [], 'jump': [], 'attack': [], 'dead': [], 'jumpAttack': [], 'walk': []}
    #     self.health_icons = {
    #         'full': pygame.transform.smoothscale(pygame.image.load(path.join(base_path, 'Tiles', 'dirt.png')), (size[0]//2, size[1]//2)),
    #         'half': pygame.transform.smoothscale(pygame.image.load(path.join(base_path, 'Tiles', 'dirtHalf.png')), (size[0]//2, size[1]//2)),
    #         'noHealth': pygame.transform.smoothscale(pygame.image.load(path.join(base_path, 'Tiles', 'boxAlt.png')), (size[0]//2, size[1]//2))
    #     }

    #     for animation in self.animations.keys():
    #         full_path = path.join(character_path, animation.capitalize())
    #         self.animations[animation] = [
    #             pygame.transform.smoothscale(
    #                 pygame.image.load(f'{full_path} ({i}).png').convert_alpha(),
    #                 size)
    #             for i in range(1, 11)]

    # def deplete_health(self, amount=1):
    #     self.current_health -= amount
    #     if self.current_health < 0:
    #         self.current_health = 0

    # def display_health(self, surface):
    #     """Displays the player's health on the given surface."""
    #     dist_x, dist_y = 30, 20
    #     for i in range(self.max_health // 2):
    #         x = dist_x * (i+1)
    #         if i < self.current_health // 2:
    #             surface.blit(self.health_icons['full'], (x, dist_y))
    #         elif i == self.current_health // 2 and self.current_health % 2 != 0:
    #             surface.blit(self.health_icons['half'], (x, dist_y))
    #         else:
    #             surface.blit(self.health_icons['noHealth'], (x, dist_y))

    # def animate(self):
    #     animation = self.animations[self.state]
    #     self.frame_index += self.animation_speed

    #     if self.frame_index >= len(animation):
    #         if self.state == 'dead':
    #             self.frame_index = len(animation) - 1
    #         elif self.state == 'attack' or self.state == 'jumpAttack':
    #             self.is_attacking = False
    #             self.state = 'idle'
    #         else:
    #             self.frame_index = 0

    #     # Flip the image based on the direction
    #     image = animation[int(self.frame_index)%len(animation)]
    #     if self.is_invincible:
    #         if (int(self.frame_index)%len(animation)) % 2 == 0:
    #             image = pygame.mask.from_surface(image).to_surface()
    #             image.set_colorkey((0,0,0))
    #             image.set_alpha(20)
    #     if self.facing_right:
    #         self.image = image
    #     else:
    #         self.image = pygame.transform.flip(image, True, False)

    # def update_state(self):
    #     if self.attacked_c and self.on_ground:
    #         self.attacked_c = 0
    #         # checking if the player has already been knocked back then no need to knock back further.
    #     if self.is_attacking:
    #         return
    #     elif self.direction.x > 0:
    #         self.facing_right = True
    #         if self.on_ground:
    #             self.state = 'run'
    #         else:
    #             self.state = 'jump'
    #     elif self.direction.x < 0:
    #         self.facing_right = False
    #         if self.on_ground:
    #             self.state = 'run'
    #         else:
    #             self.state = 'jump'
    #     else:
    #         if self.on_ground:
    #             self.state = 'idle'
    #         else:
    #             self.state = 'jump'

    #     self.is_invincible_timer = pygame.time.get_ticks()
    #     if self.is_invincible and abs(self.attacked_time - self.is_invincible_timer) > 3000:
    #         self.is_invincible = False
    #         #self.on_ground = True


    # def is_attacked(self,dir=0):
    #     attacked_time = pygame.time.get_ticks()
    #     # if the player has been knocked back or timer is up, make the player un-invincible
    #     if self.is_invincible and not self.on_ground:
    #         if abs(self.attacked_time - self.is_invincible_timer) > 3000:
    #             self.is_invincible = False
    #             self.attacked_c = 0
    #             self.attacked_dir = 0
    #     else:
    #         self.attacked_time = attacked_time
    #         self.is_invincible = True
    #         self.attacked_dir = dir
    #         self.attacked_c = 1
    #         self.current_health -= 1
    #         #self.jump()

    def get_input(self):
        # if self.is_attacking:
        #     self.direction.x = 0
        #     return
        keys = pygame.key.get_pressed()
        # mouse_buttons = pygame.mouse.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # force the player to move in the dirction of the kock back.
        # if self.is_invincible and not self.on_ground and self.attacked_c:
        #     self.direction.x = self.attacked_dir

        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            if not self.jump_key_pressed:
                self.jump()
                self.jump_key_pressed = True
        else:
            self.jump_key_pressed = False

        # # Check for attack input (left mouse click or 'F' key)
        # if mouse_buttons[0] or keys[pygame.K_f]:
        #     self.attack()

    # def attack(self):
    #     if not self.is_attacking:
    #         self.is_attacking = True
    #         if self.on_ground:
    #             self.state = 'attack'
    #         else:
    #             self.state = 'jumpAttack'
    #         self.frame_index = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        if self.on_ground:
            self.jump_count = 0

    # def jump(self,wind=0):
    def jump(self):
        if self.jump_count < self.max_jumps:
            self.direction.y = self.jump_speed
            self.on_ground = False
            self.jump_count += 1
        #     self.rect.x += wind


    def update(self):
        self.get_input()
    #     self.update_state()
    #     self.animate()
