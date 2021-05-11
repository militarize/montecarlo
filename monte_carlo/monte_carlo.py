#!/bin/env python3
# Welcome to Monte Carlo!
# We offer coin flips, and not much else!
# Watch this space for more games.
# Will add elements of expectation.

# Imports
import coin_flip

def main():
    number_of_games = int(input("How many times do you want play?: "))
    number_of_trials = int(input("Number of flips per game?: "))

    for n in range(number_of_games):
        game = coin_flip.CoinFlip()

        if (number_of_trials > 1):
            game.flip(number_of_trials)
            [heads, tails] = game.results()

            print("Game #: " + str(n+1) + "\tTotal flips: " + 
                str(number_of_trials))
            print("# of heads: " + str(heads))
            print("# of tails: " + str(tails))
        else:
            print(game.flip())

if __name__ == "__main__":
    main()
