# This will reder every single sprite
import pygame
from Config import *

class Spritesheet:
    def __init__(self, file): #Gets the file the user needs and allows them to save it as a variable
        self.sheet = pygame.image.load(file).convert()
        
    def get_sprite(self, x, y, width, height): # Then it will crop the sprite sheet by gettings the x axis, y axis the width of the image/sprite and height
        self.sheet = self.sheet
        sprite = pygame.Surface([width,height])
        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        sprite.set_colorkey('black')
        return sprite
    
class Object_renderer:
    def __init__(self, game):
        self.game = game
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        #-------ENVIRONMENT---------------
        self.snow1 = pygame.image.load('Assets/Graphics/snow1.png').convert_alpha()

        self.bush = pygame.image.load('Assets/Graphics/bush_outline.png').convert_alpha()
        self.bush_evil = pygame.image.load('Assets/Graphics/bush_evil.png').convert_alpha()

        self.road = pygame.image.load('Assets/Graphics/road1.png').convert_alpha()


        #----subsitute item----------------
        self.sub = pygame.image.load('Assets/Graphics/sub_bush.png').convert_alpha()


        #-----PLAYER-----
        self.player_down = pygame.image.load('Assets/Graphics/motorbike/noarm_down.png').convert_alpha()
        self.player_left = pygame.image.load('Assets/Graphics/motorbike/noarm_left.png').convert_alpha()
        self.player_right = pygame.image.load('Assets/Graphics/motorbike/noarm_right.png').convert_alpha()
        self.player_up = pygame.image.load('Assets/Graphics/motorbike/noarm_up.png').convert_alpha()
        self.player_arm = pygame.image.load('Assets/Graphics/motorbike/arm.png').convert_alpha()