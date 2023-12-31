# This si the main file
# imports
import pygame, sys, random, datetime
import time 
from Objects import *
from Config import  *
from Asset_renderer import *
from Level import *

#TODO: TEXT BOXES
#TODO: ENEMIES

class Main:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Christmas survivor")

        self.screen = DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.SCREEN_X, self.SCREEN_Y = DISPLAYSURF.get_size()
        self.clock = pygame.time.Clock()
        self.running = True

        self.display_surface = pygame.display.get_surface()

        self.level = Level()

        self.Power_up_dict = {'power1' : [], 'power2' : [], 'power3' : []}
    
    def run(self):
        while True:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit
            
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_pressed = pygame.mouse.get_pressed()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Main()
    game.run()