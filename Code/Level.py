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
        self.bullet_collision_sprites = pygame.sprite.Group()

        self.main_menu()
        self.story()

        self.setup()
        self.overlay = Overlay(self)

        self.time = 0

        self.bullets = []

    def story(self):
        story = True
        self.talk = 0
        self.talk1 = text_box(self,0,0 ,self.SCREEN_X,self.SCREEN_Y,"Hello! 'globmolg' you arnt dead just yet!",'white','black' )
        self.talk2 = text_box(self,0,0 ,self.SCREEN_X,self.SCREEN_Y,"You went off track when you slipped on some ice!",'white','black' )
        self.talk3 = text_box(self,0,0 ,self.SCREEN_X,self.SCREEN_Y,"Use [WASD] to move and [LMB] to shoot/ attack!",'white','black' )
        click_anywhere = self.my_font.render('click anywhere to continue!', True, 'white')

        num = 150

        self.bob = -100
        self.x_axis, self.y_axis = self.SCREEN_X // 3, self.SCREEN_Y //12#self.SCREEN_X // 3, self.SCREEN_Y //10
        self.floating = 0
        self.yug_float = 'up'

        while story:
            keys = pygame.key.get_pressed()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_pressed = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit
            self.display_surface.fill('black')

            if num == 0:
                if self.talk == 0:
                    if self.talk1.is_pressed(self.mouse_pos, self.mouse_pressed):
                        self.talk += 1
                        num = 150
                
                    self.display_surface.blit(self.talk1.image, self.talk1.rect)
                elif self.talk == 1:
                    if self.talk2.is_pressed(self.mouse_pos, self.mouse_pressed):
                        self.talk += 1
                        num = 150
                
                    self.display_surface.blit(self.talk2.image, self.talk2.rect)
                elif self.talk == 2:
                    if self.talk3.is_pressed(self.mouse_pos, self.mouse_pressed):
                        self.talk += 1
                        num = 150
                        story = False
                
                    self.display_surface.blit(self.talk3.image, self.talk3.rect)
            elif num > 0:
                num -=1
            
            if self.yug_float == 'up':
                self.y_axis -= 0.03
                self.floating += 1
                if self.floating == 200:
                    self.yug_float = 'down'
            elif self.yug_float == 'down':
                self.y_axis += 0.03
                self.floating -= 1
                if self.floating == 0:
                    self.yug_float = 'up'

            self.display_surface.blit(self.asset_loader.gob, (self.SCREEN_X // 3, self.SCREEN_Y //10 + self.y_axis))


            self.display_surface.blit(click_anywhere, (self.SCREEN_X // 4, self.SCREEN_Y - 200))

            pygame.display.update()
    
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
    
    def check_player_health(self):
        if self.player.health <= 0:
            self.dead()
    
    def dead(self):
        dead_menu = True
        title = self.title_font.render('you died!', True, 'black')
        quit_button = Button(self,(self.SCREEN_X // 6),(self.SCREEN_Y // 2),280,60,"Quit Game",'white','black' )
        play_button = Button(self,(self.SCREEN_X // 6),(self.SCREEN_Y // 3),280,60,"Back to menu",'white','black' )
        while dead_menu:
            keys = pygame.key.get_pressed()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_pressed = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit
            self.display_surface.fill('red')

            if quit_button.is_pressed(self.mouse_pos, self.mouse_pressed): # Checks to see if the player has pressed on the button
                    pygame.quit()
                    sys.exit
            
            if play_button.is_pressed(self.mouse_pos, self.mouse_pressed): # Checks to see if the player has pressed on the button
                    dead_menu = False

            self.display_surface.blit(quit_button.image, quit_button.rect)
            self.display_surface.blit(play_button.image, play_button.rect)
            self.display_surface.blit(title, (self.SCREEN_X // 6, self.SCREEN_Y // 4))
            pygame.display.update()

    def run(self, dt):
        self.time += 1
        self.check_player_health()
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bullets.append(Bullet(self.player.pos.x, self.player.pos.y, game=self))
        
        self.bullet_stuff()

        self.overlay.display()
    
    def bullet_stuff(self):
        for bullet in self.bullets[:]:
            bullet.update()
            if not self.display_surface.get_rect().collidepoint(bullet.pos):
                self.bullets.remove(bullet)
        
        for bullet in self.bullets:
            bullet.draw(self.display_surface)

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
                    if sprite == player:
                        pygame.draw.rect(self.display_surface,'red',offset_rect,5)
                        hitbox_rect = player.hitbox.copy()
                        hitbox_rect.center = offset_rect.center
                        pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)