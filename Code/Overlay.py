import pygame

from Config import *

class Overlay:
    def __init__(self, game):
        # general setup
        self.display_surface = pygame.display.get_surface()
        # self.player = player
        self.game = game
    
    def display(self):
        #display everyhting for player scrreen
        #TODO: add player health here
        player_health = self.game.my_font.render('Player Health:'+str(self.game.player.health), True, 'red')

        #Gets the player screen width and height
        x,y = self.display_surface.get_size()

        self.display_surface.blit(player_health, (x // 10, y // 7))
        
        pass