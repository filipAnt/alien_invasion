import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that represent single alien object"""

    def __init__(self, ai_game):
        """Initialize aliena and start location"""
        super().__init__()
        self.screen = ai_game.screen

        # Load image
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Load new alien at the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien position
        self.x = float(self.rect.x)
