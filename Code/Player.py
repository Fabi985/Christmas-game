import pygame
from Config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.display_surface = pygame.display.get_surface()

        self.health = MAX_PLAYER_HEALTH

        #------animation frames-----------
        self.frame_index = 0
        self.status = 'up_idle'
        
        #------HITBOX---------
        self.PLAYER_SIZE = 64
        self.image = pygame.surface.Surface((64,64))# self.animations[self.status][self.frame_index]
        self.image.fill('red')
        
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['player']

        #-----MOVEMENT--------------
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 170

        #----------HITBOX------------
        self.hitbox = self.rect.copy().inflate(12 * 2,12 * 2)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = self.status.split('_')[0] + ''dwa
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = self.status.split('_')[0] + ''
        else:
            self.direction.y = 0

            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
    
    def get_status(self):
        #if player is not moving
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
    
    def move(self, dt):
        # Normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        # horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
    
        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.image = pygame.transform.scale(self.image, (self.PLAYER_SIZE, self.PLAYER_SIZE))
        self.input()
        self.move(dt)
        self.get_status()
        # self.animate(dt)