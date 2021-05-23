# coin.py
#   This game extended the Game class and is our coin flip model.
#
# Imports
from . import game


class Coin(game.Game):
    """The quintessential coin flip.

    This class is subject to change.

    Possible future attributes:
        p = probability of H ("success", 1, etc.)
        q = 1 - p (or probability of T ("failure", 0, etc.)
    """

    def flip(self, n):
        """Returns randomly selected element from base_samples, n times."""
        pass

    def unfair_coin(self):
        """Creates an unfair coin."""
        pass
