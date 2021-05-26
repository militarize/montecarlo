# coin.py
#   This game extended the Game class and is our coin flip model.
#
# Imports
from . import game

import numpy as np

class Coin(game.Game):
    """The quintessential coin flip.

    This class is subject to change.

    Possible future attributes:
        p = probability of H ("success", 1, etc.)
        q = 1 - p (or probability of T ("failure", 0, etc.)
    """
    def __init__(self, samples, fair = True):
        """
        fair = boolean value of coin's "fairness"
            Will implement an unfair coin at some point
        """
        super(Coin, self).__init__(samples)
        if fair:
            self.fair = fair
        else:
            pass

    def flip(self, trials):
        """Returns randomly selected element from base_samples, n times."""
        results = np.random.choice(list(self.sample_space), trials)
        self.results.append(results)
        return results

    def play(self, players, trials, flips_per_trial):
        # Will merge with flip() at some point.
        """Returns randomly selected flips_per_trials, for specified number of trials, per player.

        Example: play(players = 10, trials = 10, flips_per_trial = 5)
            will run 10 trials, of 5 per trial, for 10 total players.
        """
        results = np.random.choice(list(self.sample_space), (players, trials, flips_per_trial))
        return results

    def unfair_coin(self):
        """Creates an unfair coin."""
        pass
