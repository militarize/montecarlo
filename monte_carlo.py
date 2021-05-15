#!/bin/env python3
# Welcome to Monte Carlo!
# We offer coin flips, and not much else!
# Watch this space for more games.
# Will add elements of expectation.

# Imports
from monte_carlo import coin
from monte_carlo import player
from monte_carlo import dice
from monte_carlo import distribution

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import math

def main():
    print("Implementation of Completely Fictitious Casino!")
    print("Game?")
    print("1. Coin flip")
    print("2. Random")
    print("3: Player testing")    
    print("4: Dice")
    option = int(input("Choice: "))

    if (option == 1):
        number_of_games = int(input("How many times do you want play?: "))
        number_of_trials = int(input("Number of flips per game?: "))

        for g in range(number_of_games):
            game = coin.Coin()
            print(game.game(number_of_trials))

    elif (option == 2):
        # This really is Bernoulli
        game = coin.Coin(False)
        print(game.coin_info())

        for n in range(100):
            game.flip()

        print("success: " + str(game.get_heads()))
        print("failure: " + str(game.get_tails()))
        print(game.get_results())

    elif (option == 3):
        x = int(input("How many players?: "))
        y = int(input("How many trials?: "))
        
        players = []
        for i in range(x):
            game = coin.Coin(True)
            print(game.game(y))
            
            p = player.Player()
            p.post_results(game.get_results())

            players.append(p)

        print(players)
        
        for p in players:
            print(p.get_bankroll())
            print(p.get_results())

    elif (option == 4):
        game = dice.Dice()
        game.roll(1000)
        distribution.Distribution.normal(dataset = game.get_results())

    else:
        exit()

if __name__ == "__main__":
    main()
