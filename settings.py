class Settings:
    """Class to store all game settings"""

    def __init__(self):
        """initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # Alien settings
        self.alien_speed = 1.0

        # Fleet settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Game speed settings
        self.speedup_scale = 1.1

        # Points settings
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will be updated during game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # Fleet settings
        self.fleet_direction = 1

        # Scores
        self.alien_points = 50

    def increase_speed(self):
        """Change speed and points settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
