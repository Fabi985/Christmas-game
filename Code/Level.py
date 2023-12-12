import pygame, sys
import random
from Config import *
from Overlay import *
from Player import *
from Objects import *
from Asset_renderer import *

class Level:
    def __init__(self):
        # gets the display surface
        self.display_surface = pygame.display.get_surface()
        self.SCREEN_X, self.SCREEN_Y = self.display_surface.get_size()

        #fonts
        self.my_font = pygame.font.Font('Assets/Font/PressStart2P.ttf', 25)
        self.title_font = pygame.font.Font('Assets/Font/PressStart2P.ttf', 35)

        #set up the asset loader
        self.asset_loader = Object_renderer(self)

        # sprite groups
        self.all_sprites = Camera_group()
        self.collision_sprites = pygame.sprite.Group()

        self.main_menu()

        self.setup()
        self.overlay = Overlay(self)

        self.time = 0
    
    def main_menu(self):
        menu = True
        title = self.title_font.render('Christmas survivor', True, 'black')
        quit_button = Button(self,(self.SCREEN_X // 6),(self.SCREEN_Y // 2),280,60,"Quit Game",'white','black' )
        play_button = Button(self,(self.SCREEN_X // 6),(self.SCREEN_Y // 3),280,60,"Play Game",'white','black' )
        while menu:
            keys = pygame.key.get_pressed()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_pressed = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit
            self.display_surface.fill('white')

            if quit_button.is_pressed(self.mouse_pos, self.mouse_pressed): # Checks to see if the player has pressed on the button
                    pygame.quit()
                    sys.exit
            
            if play_button.is_pressed(self.mouse_pos, self.mouse_pressed): # Checks to see if the player has pressed on the button
                    menu = False

            self.display_surface.blit(quit_button.image, quit_button.rect)
            self.display_surface.blit(play_button.image, play_button.rect)
            self.display_surface.blit(title, (self.SCREEN_X // 6, self.SCREEN_Y // 4))
            pygame.display.update()
    
    def setup(self):
        self.all_sprites.remove()
        self.tilemap = self.create_tilemap(MAP)


    def create_tilemap(self, map):
        for i, row in enumerate(map):
            for j, column in enumerate(row):
                if column == 1:
                    Generic(
                    pos = (j*TILE_SIZE, i*TILE_SIZE), 
                    surf = self.asset_loader.snow1,
                    groups = self.all_sprites,
                    z_layer = LAYERS['ground'])
                if column == 2:
                    ran = random.randint(1, 100)
                    if ran >= 15:
                        Block((j*TILE_SIZE, i*TILE_SIZE), self.asset_loader.bush, [self.all_sprites, self.collision_sprites], z = LAYERS['bush'])
                    else:
                        Bush((j*TILE_SIZE, i*TILE_SIZE), self.asset_loader.bush_evil, [self.all_sprites, self.collision_sprites], z = LAYERS['bush'], game=self, direction='left')
                if column == 'p':
                    self.player = Player((j*TILE_SIZE, i*TILE_SIZE), self.all_sprites, self.collision_sprites, self)
                    Generic(
                    pos = (j*TILE_SIZE, i*TILE_SIZE), 
                    surf = self.asset_loader.snow1,
                    groups = self.all_sprites,
                    z_layer = LAYERS['ground'])
                if column == 3:
                    Generic(
                    pos = (j*TILE_SIZE, i*TILE_SIZE), 
                    surf = self.asset_loader.snow1,
                    groups = self.all_sprites,
                    z_layer = LAYERS['ground'])
                    ran = random.randint(1, 100)
                    if ran >= 15:
                        Block((j*TILE_SIZE, i*TILE_SIZE), self.asset_loader.bush, [self.all_sprites, self.collision_sprites], z = LAYERS['bush'])
                    else:
                        Bush((j*TILE_SIZE, i*TILE_SIZE), self.asset_loader.bush_evil, [self.all_sprites, self.collision_sprites], z = LAYERS['bush'], game=self, direction='right')
                if column == 4:
                    Generic(
                    pos = (j*TILE_SIZE, i*TILE_SIZE), 
                    surf = self.asset_loader.road,
                    groups = self.all_sprites,
                    z_layer = LAYERS['ground'])

    def run(self, dt):
        self.time += 1
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()

class Camera_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self, player):
        x,y = self.display_surface.get_size()
        self.offset.x = player.rect.centerx - x / 2
        self.offset.y = player.rect.centery - y / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

                    # displays hitboxes
                    # if sprite == player:
                        # pygame.draw.rect(self.display_surface,'red',offset_rect,5)
                        # hitbox_rect = player.hitbox.copy()
                        # hitbox_rect.center = offset_rect.center
                        # pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)
                        # hitbox_arm_rect = player.arm_rect.copy()
                        # hitbox_arm_rect.center = offset_rect.center
                        # pygame.draw.rect(self.display_surface,'yellow',hitbox_arm_rect,5)