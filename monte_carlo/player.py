# Imports
import numpy as np

class Player:
    """
    Our version of the "gambler".
    Have not fleshed out or thought about this one at all.
    """
    def __init__(self, bankroll = 10000):
        self.principal = bankroll       # Initial bankroll
        self.bankroll = bankroll        # Current bankroll
        self.gain = self.bankroll - self.principal
        self.results = np.empty((1))

    def get_bankroll(self):
        return self.bankroll

    def get_roi(self):
        """
        For now, the return on investment is on the initial bankroll
        """
        return (self.gain / self.principal)

    def get_results(self):
        """
        Returns the player's actual results
        """
        return self.results

    def post_results(self, results):
        self.results = np.array(results)
