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
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate(0, 0)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE *2, TILE_SIZE*2))

class Bush(Generic):
    def __init__(self, pos, surf, groups, z, game, direction):
        super().__init__(pos, surf, groups, z)
        self.game = game
        self.pos = pos

        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate(0, 0)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE *2, TILE_SIZE*2))

        self.direction = direction
    
    def update(self, dt):
        if self.game.time == 10:
            Enemies(self.pos, self.game.asset_loader.snowmen, [self.game.all_sprites, self.game.collision_sprites], self.game, self.direction)
    

class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, game, direction):
        super().__init__(groups)
        self.game = game
        self.image = surf
        self.rect = self.image.get_rect(center = pos)

        self.hitbox = self.rect.copy()

        self.direction = direction

        self.z = LAYERS['main']

        self.num = 1   

        self.attack_cooldown = 0
    
    def update(self, dt):
        self.move(dt)
    
    def move(self, dt):
        # same y axis as player
        if self.rect.y != self.game.player.rect.y:
            if self.rect.y > self.game.player.rect.y:
                self.rect.y -= self.num
            else:
                self.rect.y += self.num
        elif self.num == self.game.player.rect.y:
            self.rect.y = self.game.player.rect.y
        
        # same x axis as player
        if self.rect.x != self.game.player.rect.x:
            if self.rect.x > self.game.player.rect.x:
                self.rect.x -= self.num
            elif self.rect.x < self.game.player.rect.x:
                self.rect.x += self.num
        elif self.rect.x == self.game.player.rect.x:
            if self.rect.y == self.game.player.rect.y:
                if self.attack_cooldown == 0:
                    self.game.player.health -= 0.5
                    self.attack_cooldown = 300
                elif self.attack_cooldown > 0:
                    self.attack_cooldown -= 1
    
class Button:
    def __init__(self,game,x, y, width, height, content, fg, bg):
        self.game = game
        #self.font = self.game.my_font # Chooses the default font
        self.content = content # The programmers text is tunred into the content, this is besically what they want the button to say.

        self.x = x # Yada Yada this is just positioning and width adn height Yada Yada
        self.y = y
        self.width = width+32
        self.height = height 

        self.fg = fg # The foreground colour
        self.bg = bg # The background olour
        self.bg2 = self.bg # The secondry background color

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.game.my_font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2,self.height/2)) # The text will be deiplasyes in the middle of the button
        self.image.blit(self.text,self.text_rect)
        

    # This si the buttons function that detects if it has been pressed and returnbd a true or false
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos): # IF the mouse is hovering over the button
            self.bg2 = 'grey' # The colour of the button will change from whatever it was to grey
            self.image.fill(self.bg2)
            self.image.blit(self.text,self.text_rect)
            if pressed[0]: # If the button is pressed it will then return true
                # self.game.sfx.play(self.game.asset_loader.click_SFX_2)
                self.image.fill(self.bg2)
                self.image.blit(self.text,self.text_rect)
                #pg.time.delay(250)
                return True
            return False
        self.image.fill(self.bg2)
        self.image.blit(self.text,self.text_rect)
        self.bg2 = self.bg
        return False # If the button was not pressed it 

class text_box:
    def __init__(self,game,x, y, width, height, content, fg, bg):
        self.game = game
        #self.font = self.game.my_font # Chooses the default font
        self.content = content # The programmers text is tunred into the content, this is besically what they want the button to say.

        self.x = x # Yada Yada this is just positioning and width adn height Yada Yada
        self.y = y
        self.width = width+32
        self.height = height 

        self.fg = fg # The foreground colour
        self.bg = bg # The background olour
        self.bg2 = self.bg # The secondry background color

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.game.my_font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2,self.height/2)) # The text will be deiplasyes in the middle of the button
        self.image.blit(self.text,self.text_rect)
        

    # This si the buttons function that detects if it has been pressed and returnbd a true or false
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos): # IF the mouse is hovering over the button
            self.bg2 = 'grey' # The colour of the button will change from whatever it was to grey
            self.image.blit(self.text,self.text_rect)
            if pressed[0]: # If the button is pressed it will then return true
                # self.game.sfx.play(self.game.asset_loader.click_SFX_2)
                self.image.blit(self.text,self.text_rect)
                #pg.time.delay(250)
                return True
            return False
        self.image.blit(self.text,self.text_rect)
        self.bg2 = self.bg
        return False # If the button was not pressed it 