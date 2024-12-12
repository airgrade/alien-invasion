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
    
    def update(self):
        '''move the bullet up the screen.'''
        
        #Update the exact position of the bullet.
        self.y = self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        '''Draw the bullet on to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)