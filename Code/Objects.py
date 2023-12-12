# This is ewhere all the objects will be held
import pygame
from Config import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z_layer = LAYERS['main']):
        super().__init__(groups)

        self.image = surf
        # self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z_layer
    
    # def update(self):
    #     self.image.draw()
    #     print("meant to darw")

class Block(Generic):
    def __init__(self, pos, surf, groups, z):
        super().__init__(pos, surf, groups, z)
        self.hitbox = self.rect.copy().inflate(-10, 0)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE *2, TILE_SIZE*2))

class Bush(Generic):
    def __init__(self, pos, surf, groups, z, game):
        super().__init__(pos, surf, groups, z)
        self.game = game
        self.pos = pos

        self.hitbox = self.rect.copy().inflate(-10, 0)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE *2, TILE_SIZE*2))
    
    def update(self, dt):
        if self.game.time == 10:
            Enemies(self.pos, pygame.surface.Surface((64,64)), self.game.all_sprites, self)
    

class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, game):
        super().__init__(groups)
        self.game = game
        self.image = surf
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

        self.hitbox = self.rect.copy()

        self.z = LAYERS['main']
    
    def update(self, dt):
        self.move()
    
    def move(self):
        self.rect.x -= self.game.game.player.rect.x