# game.py
#   Our Game class.
#
# Imports
import itertools
import enum


class Game:
    """Game class.

    To be used for general probability models. Can be extended to define subclasses of games.

    This class is subject to change.
    """

    def __init__(self, samples):
        """
        samples = iterable
            So far, we accept set{} and dict{} as data type
        """
        self.base_samples = samples
        self.sample_space = self.base_samples       # Used when constructing "newer" sample spaces.

        self.results = []                           # We are still interested in results.

    def get_sample_space(self):
        """Returns the current sample space for the game."""
        return self.sample_space

    def new_sample_space(self, n):
        """Updates sample_space to combos of base_samples of n length.

        This method is subject to change. There are concerns for speed.
        """
        self.sample_space = set([i for i in itertools.product(self.base_samples, repeat = n)])

    def get_results(self):
        """Returns current results for the "lifetime" of the game."""
        return self.results
