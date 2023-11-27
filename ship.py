import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings 

        #load the ship's image and rect -- rect is to make a rectangle
        self.image = pygame.image.load('images/Spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start the ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #stores a decimal value for the ship's center soalny td kan gnti jd 1.5px (not an integer anymore)
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Updates the ship position if prompt to"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            #the rect kan rectangle, itu ttp ditengahin jd rectny pinda kanan/kiri so the ship is still ditenga rectny

        #updates rect obkect frpm self.center
        self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship at its current location (in this case center bottom cuz of self rect centerx and bottom)"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx