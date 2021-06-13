import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that represent single alien object"""

    def __init__(self, ai_game):
        """Initialize aliena and start location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load image
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Load new alien at the top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien position
        self.x = float(self.rect.x)

    def update(self):
        """Move alien right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if alien is on the edge of screen"""
        screen_react = self.screen.get_rect()
        if self.rect.right >= screen_react.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to left or right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x