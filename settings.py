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