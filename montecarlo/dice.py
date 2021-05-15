# Imports
import numpy as np

class Dice:
    """Really basic dice implementation that suffices for now."""

    def __init__(self, n_dice = 1):
        self.n_dice = n_dice            # of dice per throw
        self.results = []               # results of all throws
        #self.n_sides = n_sides         # of sides of each die

    def roll(self, n_rolls = 1):
        """n_rolls of n_dice."""
        for roll in range(n_rolls):
            total = 0
            for i in range(self.n_dice):
                total += np.random.randint(1, 7, dtype = np.int8)
            self.results.append(total)

    def get_results(self):
        """Returns a list of all dice throws."""
        return self.results
