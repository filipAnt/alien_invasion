"""First project - creation of simple game - alien invasion
based on book Python Crash Course, 2nd Edition"""

import sys
import pygame
from settings import Settings


class Alieninvasion:
    """Main class to manage game resources"""

    def __init__(self):
        """create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Main game loop"""
        while True:
            # Wait unitl user will press Enter key or mouse button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refresh game screen
            self.screen.fill(self.settings.bg_color)

            # Display last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # Run game
    ai = Alieninvasion()
    ai.run_game()
