import pygame, math
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
        self.image = self.game.asset_loader.player_up#pygame.surface.Surface((64,64))# self.animations[self.status][self.frame_index]wa
        self.player_arm = self.game.asset_loader.player_arm
        
        self.rect = self.image.get_rect(center = pos)
        self.x,self.y = self.display_surface.get_size()
        self.arm_rect = (self.x // 2)-9, (self.y // 2)+9
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
            self.status = 'up'
            self.image = self.game.asset_loader.player_up
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
            self.image = self.game.asset_loader.player_down
        else:
            self.direction.y = 0

            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
            self.image = self.game.asset_loader.player_right
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
            self.image = self.game.asset_loader.player_left
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
    
    def draw_arm(self):
        self.player_arm = pygame.transform.scale(self.player_arm, (5*2, 11*4)) 
        # self.game.display_surface.blit(self.player_arm, self.arm_rect)
        if self.status == 'down' or self.status == 'down_idle':
            self.arm_rect = (self.x // 2)-9, (self.y // 2)+9
        elif self.status == 'up' or self.status == 'up_idle':
            self.arm_rect = (self.x // 2)-20, (self.y // 2)+20
        
        pos = pygame.mouse.get_pos()
        angle = 360-math.atan2(pos[1]-(self.y // 2)+34,pos[0]-(self.x // 2)-6)*180/math.pi
        self.rotimage = pygame.transform.rotate(self.player_arm, angle)
        self.arm_rect = self.rotimage.get_rect(center=((self.x // 2)-6, (self.y // 2)+34))
        self.game.display_surface.blit(self.rotimage, self.arm_rect) 

    def update(self, dt):
        self.input()
        self.move(dt)
        self.get_status()
        if self.status == 'left' or self.status == 'right' or self.status == 'right_idle' or self.status == 'left_idle':
            self.image = pygame.transform.scale(self.image, (self.PLAYER_SIZE*2, self.PLAYER_SIZE))
        else:
            self.image = pygame.transform.scale(self.image, (self.PLAYER_SIZE, self.PLAYER_SIZE*2))

        #draw arm
        self.draw_arm()