#!/bin/env python3 
# We simulate coin flips.
# Sounds boring. But as an introduction to randomness, quite elegant.
import random

class CoinFlip:

    def __init__(self):
        self.number_of_heads = 0
        self.number_of_tails = 0

        # Use the coin flip itself to determine if the coin itself will be fair.
        if (random.randint(0, 1) == 0):
            self.fair = False
            self.percent_of_heads = random.random()
        else:
            self.fair = True
            self.percent_of_heads = 0.5

    def flip(self, n = 1):
        if self.fair:
            if n > 1:
                for i in range(0, n):
                    toss = random.randint(0, 1)
 
                    if toss == 1:
                        self.number_of_heads += 1
                    else:
                        self.number_of_tails += 1
            else:
                return random.randint(0, 1)
        if not self.fair:
            if n > 1:
                for i in range(0, n):
                    toss = random.random()

                    if toss <= self.percent_of_heads:
                        self.number_of_heads += 1
                    else:
                        self.number_of_tails += 1
            else:
                toss = random.random()

                if toss <= self.percent_of_heads:
                    return 1
                else:
                    return 0

    def results(self):
        return [self.number_of_heads, self.number_of_tails]

    def is_coin_fair(self):
        return [self.fair, self.percent_of_heads]
