class GameStats:
    """Collect data for game statistics"""

    def __init__(self, ai_game):
        """initialize statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Run game in inactive state
        self.game_active = False

    def reset_stats(self):
        """initialize data that can be updated while game is running"""
        self.ships_left = self.settings.ship_limit
        self.score = 0