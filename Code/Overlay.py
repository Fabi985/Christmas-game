import pygame

from Config import *

class Overlay:
    def __init__(self):
        # general setup
        self.display_surface = pygame.display.get_surface()
        # self.player = player
    
    def display(self):
        #display everyhting for player scrreen
        #TODO: add player health here
        #TODO: add player inventory here

        #Gets the player screen width and height
        x,y = self.display_surface.get_size()
        
        pass