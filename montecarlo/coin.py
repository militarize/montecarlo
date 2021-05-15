#!/bin/env python3 
# We simulate coin flips.
# Sounds boring. But as an introduction to randomness, quite elegant.
# This module will (hopefully) be improved upon.

# Imports
import numpy as np

class Coin:
    """The quintessential coin flip."""

    def __init__(self, fair = True):
        """Initialize all coin attributes.

        p = probability of "heads" (success)
        q = 1 - p
        """

        self.fair = fair                # fairness value of the coin
        self.number_of_heads = 0        # of successes
        self.number_of_tails = 0        # of failures

        # Standardize to DataFrame eventually:
        self.values = []
        
        if fair:
            self.p = 0.5
            self.q = 0.5
        else:
            self.p = int(np.random.random() * 10) / 10.00
            self.q = 1 - self.p

    def flip(self):
        """A single flip of the coin.

        Returns result of the toss.
        """

        # flip() and game() will likely be amalgamated into one method.

        toss = int(np.random.random() * 10) / 10.00

        if (toss < self.p):
            self.number_of_heads += 1
        else:
            self.number_of_tails += 1

        self.values.append(toss)
        return toss

    def game(self, n_trials):
        """Multiple flips of the coin.

        Returns the results.
        """

        if self.fair:
            self.values = np.random.randint(2, size = n_trials)
        else:
            results = np.random.rand(n_trials)
            for i in range(len(results)):
                results[i] = int(results[i] * 10) / 10.00
            self.values = results

        return self.values

    def get_results(self):
        """Returns all of the results of the coin."""
        return self.values

    def get_heads(self):
        """Returns the number of heads on the coin."""
        return self.number_of_heads

    def get_tails(self):
        """Returns the number of tails on the coin."""
        return self.number_of_tails

    def coin_info(self):
        """Returns a coin's information: fairness value and probabilities."""
        return [self.fair, self.p, self.q]
