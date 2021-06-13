import pygame

class Ship:
    """Class to manage space ship"""
    def __init__(self, ai_game):
        """init space ship and start location"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # New ship start at the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display ship in actual position"""
        self.screen.blit(self.image, self.rect)