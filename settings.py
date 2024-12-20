class Settings:
    '''A class to store all settings for alien invasion'''
    
    def __init__(self):
        '''A function to initialize the game settings.'''
        #Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed = 1.5
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)