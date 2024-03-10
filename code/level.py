import pygame
from tiles import Tile
from settings import *
from player import Player
# from enemies import Enemy
# from Door import Door

class Level:
    def __init__(self, level_data, surface):
        # Level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # self.enemies = pygame.sprite.Group()
        # self.doors = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                # elif cell == 'E':
                #     enemy = Enemy((x,y))
                #     self.enemies.add(enemy)
                # elif cell == 'J':
                #     door_sprite = Door((x, y))
                #     self.doors.add(door_sprite)
                elif cell != ' ':
                    tile_sprite = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile_sprite)


    # def scroll_x(self):
    #     player = self.player.sprite
    #     player_x = player.rect.centerx
    #     direction_x = player.direction.x

    #     if player_x < screen_width/4 and direction_x < 0:
    #         self.world_shift = 8
    #         player.speed = 0
    #     elif player_x > screen_width - (screen_width/4) and direction_x > 0:
    #         self.world_shift = -8
    #         player.speed = 0
    #     else:
    #         self.world_shift = 0
    #         player.speed = 4


    # def horizontal_enemy_collision(self):
    #     for enemy in self.enemies.sprites():
    #         enemy.move()  # Move the enemy horizontally
    #         # Check for collisions with tiles after adjusting direction

    #         for sprite in self.tiles.sprites():
    #             if enemy.rect.colliderect(sprite.rect):
    #                 # Adjust position if there's a collision
    #                 if enemy.direction.x < 0:
    #                     enemy.rect.left = sprite.rect.right
    #                     # enemy.direction.x = 1
    #                     enemy.flip()
    #                 elif enemy.direction.x > 0:
    #                     enemy.rect.right = sprite.rect.left
    #                     # enemy.direction.x = -1
    #                     enemy.flip()
    #             else:
    #                 self.is_tile_below(enemy)
            # Check if there's a tile below the enemy

    # def is_tile_below(self, enemy):
    #     # Calculate the position of the tile below the enemy

    #     if enemy.facing == 'left':
    #         tile_below_x = enemy.rect.x
    #     elif enemy.facing == 'right':
    #         tile_below_x = enemy.rect.x + enemy.rect.width

    #     tile_below_y = enemy.rect.y + tile_size

    #     # Iterate through all tiles to check for collision with the tile below
    #     for tile in self.tiles.sprites():
    #         if tile.rect.collidepoint(tile_below_x, tile_below_y):
    #             break  # There is a tile below, no need to reverse direction
    #     else:
    #         # If no tile below, flip the enemy
    #             enemy.flip()

    # def check_door_collision(self):
    #     player = self.player.sprite
    #     doors = self.doors.sprites()

    #     for door in doors:
    #         if pygame.sprite.collide_rect(player, door):
    #             keys = pygame.key.get_pressed()
    #             if keys[pygame.K_SPACE]:
    #                 self.change_level()  # Change the level when the player interacts with the door
                    
    # def change_level(self):
    #     # Clear all sprite groups
    #     self.tiles.empty()
    #     self.player.empty()
    #     self.enemies.empty()
    #     self.doors.empty()

    #     # Load the new level data
    #     self.setup_level(level_map2)
    
    # def vertical_enemy_collision(self):
    #     for enemy in self.enemies.sprites():
    #         temp_rect = enemy.rect.copy()
    #         temp_rect.y += 1
    #         flag = False
    #         for sprite in self.tiles.sprites():
    #             if sprite.rect.colliderect(temp_rect):
    #                 enemy.on_ground = True
    #                 flag = True
    #         if not flag:
    #             if enemy.direction.x < 0:
    #                 enemy.direction.x = 1
    #             elif enemy.direction.x > 0:
    #                 enemy.direction.x = -1

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 # this statement makes sure apply gravity doesn't make player.direction.y too large
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 # this statement ensure tht if the player's top hit bottom of a tile, then it will fall


    # def horizontal_movement_collision(self):
    #     player = self.player.sprite
    #     player.rect.x += player.direction.x * player.speed

    #     #merging knock back, wall collision and invisble frames
    #     for enemy in self.enemies.sprites():
    #         for sprite in self.tiles.sprites():
    #             if enemy.rect.colliderect(player.rect) and not player.is_invincible:

                    
    #                 # check if player is on the left of enemy or right and knock in that direction
    #                 if player.rect.left >= enemy.rect.left: 
    #                     #player.direction.x = 1
    #                     #player.direction.y = -15
    #                     #player.rect.x += player.direction.x * player.speed * 2

    #                     #setting up invisble frames after kock back
    #                     player.is_attacked(1)
    #                     #flip enemy upon collision
    #                     if enemy.direction.x < 0:
    #                         enemy.direction.x = 1
    #                     elif enemy.direction.x > 0:
    #                         enemy.direction.x = -1

                        
    #                 elif player.rect.left <= enemy.rect.left:
    #                     #player.direction.x = -1
    #                     #player.direction.y = -15
    #                     #player.rect.x += player.direction.x * player.speed * 2

    #                     player.is_attacked(-1)
    #                     if enemy.direction.x < 0:
    #                         enemy.direction.x = 1
    #                     elif enemy.direction.x > 0:
    #                         enemy.direction.x = -1

    #                 player.jump()
    #                 player.on_ground = False
    #             # check collision with the wall 
    #             if sprite.rect.colliderect(player.rect) and sprite != self.doors.sprite:
    #                 if player.direction.x < 0:
    #                     player.rect.left = sprite.rect.right
    #                     self.world_shift = 0
    #                 elif player.direction.x > 0:
    #                     player.rect.right = sprite.rect.left
    #                     self.world_shift = 0

       
    # def vertical_movement_collision(self):
    #     player = self.player.sprite
    #     player.apply_gravity()

    #     #merging vertical knock back, wall collision and invislbe frames
    #     for enemy in  self.enemies.sprites():
    #         for sprite in self.tiles.sprites():
    #             if enemy.rect.colliderect(player.rect) and not player.is_invincible:
    #                 if player.rect.left <= enemy.rect.left:
    #                     #player.direction.y = -15
    #                     player.is_attacked(-1)
    #                     if enemy.direction.x < 0:
    #                         enemy.direction.x = 1
    #                     elif enemy.direction.x > 0:
    #                         enemy.direction.x = -1
    #                 elif player.rect.left >= enemy.rect.left:
    #                     #player.direction.y = -15
    #                     player.is_attacked(1)
    #                     if enemy.direction.x < 0:
    #                         enemy.direction.x = 1
    #                     elif enemy.direction.x > 0:
    #                         enemy.direction.x = -1
    #                 player.jump()
    #                 player.on_ground = False                    
    #             if sprite.rect.colliderect(player.rect):
    #                 if player.direction.y > 0:
    #                     player.rect.bottom = sprite.rect.top
    #                     player.direction.y = 0 # this statement makes sure apply gravity doesn't make player.direction.y too large
    #                     player.on_ground = True
    #                 elif player.direction.y < 0:
    #                     player.rect.top = sprite.rect.bottom
    #                     player.direction.y = 0 # this statement ensure tht if the player's top hit bottom of a tile, then it will fall

    #     if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
    #         player.on_ground = False

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # # Doors
        # self.doors.draw(self.display_surface)
        # self.doors.update(self.world_shift)
        
        # # Player
        # self.scroll_x() # scroll_x before horizontal_movement_collision for moving screen
        # self.check_door_collision()  # Check for door collisions
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        # self.player.sprite.display_health(self.display_surface)

        # # Enemy
        # self.vertical_enemy_collision()
        # self.horizontal_enemy_collision()
        # self.enemies.update(self.world_shift)
        # self.enemies.draw(self.display_surface)
