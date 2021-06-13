import pygame

class Ship:
    """Class to manage space ship"""
    def __init__(self, ai_game):
        """init space ship and start location"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # New ship start at the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship location
        self.x = float(self.rect.x)

        # Check if ship is moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship location based on move"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update ship location x
        self.rect.x = self.x

    def blitme(self):
        """Display ship in actual position"""
        self.screen.blit(self.image, self.rect)