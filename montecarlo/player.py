# Imports
import numpy as np

class Player:
    """The "gambler" class.

    This class will eventually contain all attributes related to the player,
    including: bankroll and bankroll fluctuations, returns, and results.
    """

    def __init__(self, bankroll = 10000):
        self.principal = bankroll                       # Initial bankroll
        
        # Will eventually implement data structure (DataFrame) to track:
        self.bankroll = bankroll                        # Current bankroll
        self.gain = self.bankroll - self.principal      # "Dollar" gain/loss
        
        # Standardize to pandas DataFrame eventually:
        self.results = np.empty((1))

    def get_bankroll(self):
        """Returns current bankroll amount."""
        return self.bankroll

    def get_roi(self):
        """Returns the player's return on investment.

        For now, the return on investment is on the initial bankroll.
        """

        return (self.gain / self.principal)

    def get_results(self):
        """Returns the player's actual results."""
        return self.results

    def post_results(self, results):
        """Implementation of a very temporary and rudimentary results system.

        No actual bet system implemented yet. A win/loss is +/-500 for now.
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
