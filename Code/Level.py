import pygame
from Config import *
from Overlay import *
from Player import *
from Objects import *

class Level:
    def __init__(self):
        # gets the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = Camera_group()

        self.setup()
        self.overlay = Overlay()
    
    def setup(self):
        self.player = Player((0,0), self.all_sprites)


    def create_tilemap(self):
        for i, row in enumerate(MAP):
            for j, column in enumerate(row):
                if column == 1:
                    Generic(
                    pos = (0,0), 
                    surf = pygame.image.load('').convert_alpha(),
                    groups = self.all_sprites,
                    z_layer = LAYERS['ground'])

    def run(self, dt):
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
        # self.offset.x = player.rect.centerx - x / 2
        # self.offset.y = player.rect.centery - y / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

                    # displays hitboxes
                    if sprite == player:
                        pygame.draw.rect(self.display_surface,'red',offset_rect,5)
                        hitbox_rect = player.hitbox.copy()
                        hitbox_rect.center = offset_rect.center
                        pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)