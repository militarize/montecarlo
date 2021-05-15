# Imports
import numpy as np

class Dice:
    """
    Really basic dice implementation that suffices for now.
    """
    def __init__(self, n_dice = 2):
        self.n_dice = 2
        self.results = []

    def roll(self, n_rolls = 1):
        for roll in range(n_rolls):
            total = 0
            for i in range(self.n_dice):
                total += np.random.randint(1, 7, dtype = np.int8)
            self.results.append(total)

    def get_results(self):
        return self.results
