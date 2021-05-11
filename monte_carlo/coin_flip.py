#!/bin/env python3 
# We simulate coin flips.
# Sounds boring. But as an introduction to randomness, quite elegant.
import random

class CoinFlip:

    def __init__(self):
        self.number_of_heads = 0
        self.number_of_tails = 0
 
    def flip(self, n):
        for i in range(0, n):
            toss = random.randint(0, 1)
 
            if toss == 1:
                self.number_of_heads += 1
            else:
                self.number_of_tails += 1
 
        #print("Number of heads: " + str(number_of_heads) + "\t% heads: " + 
        #    str("{:.16f}".format(number_of_heads / n)))
        #print("Number of tails: " + str(number_of_tails) + "\t% tails: " + 
        #    str("{:.16f}".format(number_of_tails / n)))

    def results(self):
        return [self.number_of_heads, self.number_of_tails]
