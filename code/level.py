import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player
from enemies import Enemy

class Level:
    def __init__(self, level_data, surface):
        # Level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == 'E':
                    enemy = Enemy((x,y))
                    self.enemies.add(enemy)
                elif cell != ' ':
                    tile_sprite = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    # def horizontal_enemy_collision(self):
    #     for enemy in self.enemies.sprites():
    #         enemy.move()
    #         colidables = self.tiles.sprites()
    #         for  sprite in colidables:
    #             if enemy.rect.colliderect(sprite.rect):
    #                 if enemy.direction.x < 0:
    #                     enemy.rect.left = sprite.rect.right
    #                     enemy.direction.x = 1
    #                     self.on_left = True
    #                 elif enemy.direction.x > 0:
    #                     enemy.rect.right = sprite.rect.left
    #                     enemy.direction.x = -1
    #                     self.on_right = True

    def horizontal_enemy_collision(self):
        for enemy in self.enemies.sprites():
            enemy.move()  # Move the enemy horizontally
            # Check for collisions with tiles after adjusting direction

            for sprite in self.tiles.sprites():
                if enemy.rect.colliderect(sprite.rect):
                    # Adjust position if there's a collision
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                        # enemy.direction.x = 1
                        enemy.flip()
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                        # enemy.direction.x = -1
                        enemy.flip()
                else:
                    self.is_tile_below(enemy)
            # Check if there's a tile below the enemy

    def is_tile_below(self, enemy):
        # Calculate the position of the tile below the enemy

        if enemy.facing == 'left':
            tile_below_x = enemy.rect.x
        elif enemy.facing == 'right':
            tile_below_x = enemy.rect.x + enemy.rect.width

        tile_below_y = enemy.rect.y + tile_size

        # Iterate through all tiles to check for collision with the tile below
        for tile in self.tiles.sprites():
            if tile.rect.collidepoint(tile_below_x, tile_below_y):
                break  # There is a tile below, no need to reverse direction
        else:
            # If no tile below, flip the enemy
                enemy.flip()

    def vertical_enemy_collision(self):
        for enemy in self.enemies.sprites():
            temp_rect = enemy.rect.copy()
            temp_rect.y += 1
            flag = False
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(temp_rect):
                    enemy.on_ground = True
                    flag = True
            if not flag:
                if enemy.direction.x < 0:
                    enemy.direction.x = 1
                elif enemy.direction.x > 0:
                    enemy.direction.x = -1


    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        #setup invisible frames
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and not player.is_invincible:
                player.is_attacked()
                if enemy.direction.x < 0:
                    enemy.direction.x = 1
                    self.on_left = True
                elif enemy.direction.x > 0:
                    enemy.direction.x = -1
                    self.on_right = True
            
                
        #setup horizontal player knock back colision.
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and not player.is_invincible:
                for sprite in self.tiles.sprites():
                    if not abs(sprite.rect.x - enemy.rect.x) <= 64:
                        continue # checking only nearby tiles
                    if enemy.direction.x < 0 and player.rect.left - 5 <= sprite.rect.right and sprite.rect.right <= enemy.rect.left:
                        player.rect.left = sprite.rect.right
                    elif enemy.direction.x > 0 and player.rect.right + 5 >= sprite.rect.left and sprite.rect.left >= enemy.rect.right:
                        player.rect.right = sprite.rect.left
                    elif enemy.direction.x < 0:
                        player.direction.x = -5
                    elif enemy.direction.x > 0:
                        player.direction.x = 5
                    player.jump()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.world_shift = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.world_shift = 0
    
    def knock_back(self):
        pass
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        # vertical kockback
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and not player.is_invincible:
                if enemy.direction.x < 0:
                    player.direction.x = -5
                    player.direction.y = 0
                elif enemy.direction.x > 0:
                    player.direction.x = 5
                    player.direction.y = 0
                player.rect.x += player.direction.x * (player.speed//4)
                player.jump()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 # this statement makes sure apply gravity doesn't make player.direction.y too large
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 # this statement ensure tht if the player's top hit bottom of a tile, then it will fall

        # if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
        #     player.on_ground = False
        # if player.on_ceiling and player.direction.y > 0:
        #     player.on_ceiling = False

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.scroll_x() # scroll_x before horizontal_movement_collision for moving screen
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        # Enemy
        self.vertical_enemy_collision()
        self.horizontal_enemy_collision()
        self.enemies.update(self.world_shift)
        self.enemies.draw(self.display_surface)
