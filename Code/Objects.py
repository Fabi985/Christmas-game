# This is ewhere all the objects will be held
import pygame
from Config import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z_layer = LAYERS['main']):
        super().__init__(groups)

        self.image = surf
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z_layer