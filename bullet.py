import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """ini makes the bullet object at posisi shipny"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Creates a bullet rect at (0,0) then sets it to the position of the ship
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx #bullet's centerx ditengah shipny cuz same loc as the ship's centerx
        self.rect.top = ship.rect.top #ini spya diatas shipny so it looks like the bullets r being fired from the ship

        #stores the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """Moves the bullet up the screen (ya ditembak)"""
        #update decimal position of bullet
        self.y -= self.speed_factor #ini for whatever stupid reason klo naik - kl kebawah + gajelas python
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
