#!/bin/env python3 
# We simulate coin flips here.
# Sounds boring. But as an introduction to randomness, quite elegant.
# This module will (hopefully) be improved upon.

# Imports

class Coin:
    """The quintessential coin flip.

    This class is subject to change.

    Current attributes:
        fair = boolean value respresenting fairness of the coin
        base_samples = all possible base outcomes (for a coin: { "H", "T" })

    Possible future attributes:
        p = probability of H ("success", 1, etc.)
        q = 1 - p (or probability of T ("failure", 0, etc.)
    """

    def __init__(self, fair = True):

        self.fair = fair                        # Default to True (it IS a coin)
        self.base_samples = { "H", "T" }

    def is_heads(self, event):
        """Returns True if "event" is heads."""

        return (event in self.base_samples)
