import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage the bullets fired from the ship'''
    
    def __init__(self, ai_game):
        '''Create a bullet object from the ships current position.'''
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Create a bullet rectangle at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Store bullets postion as a float
        self.y = float(self.rect.y)
    