import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.CHARACTER_WIDTH = 50
        self.CHARACTER_HEIGHT = 60
        self.import_character_assets((self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT))

        # Player animation state
        self.state = 'idle'
        self.facing_right = True
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

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

        self.is_attacking = False

    def import_character_assets(self,size:(int,int)):
        character_path = ''
        self.animations = {'idle': [], 'run': [], 'jump': [], 'attack': [], 'dead': [], 'jumpAttack': [], 'walk': []}

        for animation in self.animations.keys():
            full_path = character_path + animation.capitalize()
            self.animations[animation] = [
                pygame.transform.smoothscale(
                    pygame.image.load(f'{full_path} ({i}).png'),
                    size)
                for i in range(1, 11)]

    def animate(self):
        animation = self.animations[self.state]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            if self.state == 'dead':
                self.frame_index = len(animation) - 1
            elif self.state == 'attack' or self.state == 'jumpAttack':
                self.is_attacking = False
                self.state = 'idle'
            else:
                self.frame_index = 0

        # Flip the image based on the direction
        image = animation[int(self.frame_index)%len(animation)]
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    def update_state(self):
        if self.is_attacking:
            return
        elif self.direction.x > 0:
            self.facing_right = True
            if self.on_ground:
                self.state = 'run'
            else:
                self.state = 'jump'
        elif self.direction.x < 0:
            self.facing_right = False
            if self.on_ground:
                self.state = 'run'
            else:
                self.state = 'jump'
        else:
            if self.on_ground:
                self.state = 'idle'
            else:
                self.state = 'jump'

    def get_input(self):
        if self.is_attacking:
            self.direction.x = 0
            return
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()

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

        # Check for attack input (left mouse click or 'F' key)
        if mouse_buttons[0] or keys[pygame.K_f]:
            self.attack()

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            if self.on_ground:
                self.state = 'attack'
            else:
                self.state = 'jumpAttack'
            self.frame_index = 0

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
        self.update_state()
        self.animate()
