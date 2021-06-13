"""First project - creation of simple game - alien invasion
based on book Python Crash Course, 2nd Edition"""

import sys
import pygame
from settings import Settings
from ship import Ship


class Alieninvasion:
    """Main class to manage game resources"""

    def __init__(self):
        """create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Main game loop"""
        while True:
            # Refresh loop for every iteration
            self._check_events()
            self._update_screen()

            # Refresh game screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Display last modified screen
            pygame.display.flip()

    def _check_events(self):
        """React on mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Screen update"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == '__main__':
    # Run game
    ai = Alieninvasion()
    ai.run_game()
