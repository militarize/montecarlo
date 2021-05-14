#!/bin/env python3 
# We simulate coin flips.
# Sounds boring. But as an introduction to randomness, quite elegant.
from numpy import random

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
            self.p = int(random.random() * 10) / 10.00
            self.q = 1 - self.p

    def flip(self, n = 1):
        for i in range(0, n):
            toss = int(random.random() * 10) / 10.00

            if (toss < self.p):
                self.number_of_heads += 1
            else:
                self.number_of_tails += 1

            self.values.append(toss)

    # Work with one one array at a time? Or generate all of them at once?
    def game(self, number_of_trials):
        if self.fair:
            self.values = random.randint(2, size = number_of_trials)
        else:
            results = random.rand(number_of_trials)
            for i in range(len(results)):
                results[i] = int(results[i] * 10) / 10.00
            self.values = results

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
