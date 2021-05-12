#!/bin/env python3 
# We simulate coin flips.
# Sounds boring. But as an introduction to randomness, quite elegant.
import random

class CoinFlip:

    def __init__(self, fair = True):
        """
        p = probability of "heads" (success)
        q = 1 - p
        
        fair = True or False
        """
        self.fair = fair
        self.number_of_heads = 0        # of successes
        self.number_of_tails = 0        # of failures

        # values matrix containing success/failure and value?
        self.values = []
        
        if fair:
            self.p = 0.5
            self.q = 0.5
        else:
            self.p = random.random()
            self.q = 1 - self.p

    def flip(self, n = 1):
        for i in range(0, n):
            toss = random.random()

            if (toss <= self.p):
                self.number_of_heads += 1
            else:
                self.number_of_tails += 1

            self.values.append(toss)

    def get_results(self):
        return self.values

    def get_heads(self):
        return self.number_of_heads

    def get_tails(self):
        return self.number_of_tails

    def coin_info(self):
        """
        Returns a coin's information: fairness value and probabilities
        """
        return [self.fair, self.p, self.q]
