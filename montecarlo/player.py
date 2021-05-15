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
        """
        Very rudimentary results system for now.
        No actual bet system implemented yet. A win is +500 for now.
        """
        self.results = np.array(results)
        for result in results:
            if self.bankroll:
                if result:
                    self.bankroll += 500
                elif self.bankroll < 500:         # To be changed later
                    self.bankroll = 0
                else:
                    self.bankroll -= 500
            else:
                print("Insufficient funds!")
                break
