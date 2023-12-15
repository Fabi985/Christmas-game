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

        #--------PLAYER HEALTH----------
        self.heart = pygame.image.load('Assets/Graphics/heart_done.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (128, 128))

        self.health_bar = pygame.image.load('Assets/Graphics/health_bar.png').convert_alpha()
        self.health_bar = pygame.transform.scale(self.health_bar, (300*2, 215))

        #----gob----
        self.gob = pygame.image.load('Assets/Graphics/christmas yug.png').convert_alpha()
        self.gob = pygame.transform.scale(self.gob, (320, 320))
    
        #------enemies----
        self.snowmen = pygame.image.load('Assets/Graphics/enemies/mr_stabby.png').convert_alpha()
        self.snowmen = pygame.transform.scale(self.snowmen, (TILE_SIZE, TILE_SIZE))

        self.snowmen2 = pygame.image.load('Assets/Graphics/enemies/gangsta snowman.png').convert_alpha()
        self.snowmen2 = pygame.transform.scale(self.snowmen2, (TILE_SIZE, TILE_SIZE))

        self.snowmen3 = pygame.image.load('Assets/Graphics/enemies/snowballa.png').convert_alpha()
        self.snowmen3 = pygame.transform.scale(self.snowmen3, (TILE_SIZE, TILE_SIZE))

        self.ginger = pygame.image.load('Assets/Graphics/enemies/gingerbread man.png').convert_alpha()
        self.ginger = pygame.transform.scale(self.ginger, (TILE_SIZE, TILE_SIZE))

        self.JERMY = pygame.image.load('Assets/Graphics/enemies/JERMA.png').convert_alpha()
        self.JERMY = pygame.transform.scale(self.JERMY, (TILE_SIZE, TILE_SIZE))

        #-----PLAYER-----
        self.player_down = pygame.image.load('Assets/Graphics/motorbike/boike_down.png').convert_alpha()
        self.player_left = pygame.image.load('Assets/Graphics/motorbike/boike_left.png').convert_alpha()
        self.player_right = pygame.image.load('Assets/Graphics/motorbike/boike_right.png').convert_alpha()
        self.player_up = pygame.image.load('Assets/Graphics/motorbike/boike_up.png').convert_alpha()
        self.player_arm = pygame.image.load('Assets/Graphics/motorbike/arm.png').convert_alpha()


        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        self.music1 = pygame.mixer.Sound('Assets/Music/y2mate.is - Kavinsky Nightcall 8 BIT Music By FRANKJAVCEE -dUpP80Y8YIQ-192k-1702564096-[AudioTrimmer.com]-[AudioTrimmer.com] 2.wav')