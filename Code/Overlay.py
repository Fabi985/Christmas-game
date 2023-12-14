import pygame, math

from Config import *

class Overlay:
    def __init__(self, game):
        # general setup
        self.display_surface = pygame.display.get_surface()
        # self.player = player
        self.game = game
    
    def display(self):
        #Gets the player screen width and height
        x,y = self.display_surface.get_size()

        #display everyhting for player scrreen
        #TODO: add player health here
        player_health = self.game.my_font.render('Player Health:'+str(round(self.game.player.health)), True, 'red')
        pygame.draw.rect(self.display_surface,'red',(x // 10, y // 7, (self.game.player.health* 2) , 20 ))

        self.display_surface.blit(self.game.asset_loader.health_bar, (x // 28, y // 16))
        self.display_surface.blit(self.game.asset_loader.heart, (x // 13, y // 10))
        # self.display_surface.blit(player_health, (x // 10, y // 7))

        #timer
        pygame.draw.rect(self.display_surface,'orange',(0, 0, (self.game.timer* 7) , 20 ))
        
        pass