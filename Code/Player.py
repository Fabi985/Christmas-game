import pygame
from Config import *
from Asset_renderer import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, game):
        super().__init__(group)
        self.game = game

        self.display_surface = pygame.display.get_surface()

        self.health = MAX_PLAYER_HEALTH

        #------animation frames-----------
        self.frame_index = 0
        self.status = 'up_idle'
        
        #------HITBOX---------
        self.PLAYER_SIZE = 64
        self.image = self.game.asset_loader.player_idle#pygame.surface.Surface((64,64))# self.animations[self.status][self.frame_index]wa
        self.player_arm = self.game.asset_loader.player_arm
        
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['player']

        #-----MOVEMENT--------------
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 350

        self.collision_sprites = collision_sprites

        #----------HITBOX------------
        self.hitbox = self.rect.copy().inflate(50, 50)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = self.status.split('_')[0] + ''
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

        # horizontal movment
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')
    
    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0: #moving right
                            self.hitbox.right = sprite.hitbox.left
                        elif self.direction.x < 0:#moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    
                    if direction == 'vertical':
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        elif self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def update(self, dt):
        self.image = pygame.transform.scale(self.image, (self.PLAYER_SIZE, self.PLAYER_SIZE*2))
        self.input()
        self.move(dt)
        self.get_status()
        # self.animate(dt)