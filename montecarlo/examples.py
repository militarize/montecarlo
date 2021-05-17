#!/bin/env python3
# Welcome to Monte Carlo!
# We offer coin flips, and not much else!
# Watch this space for more games.

# Imports
from game import coin

def main():
    """Welcome to Monte Carlo.

    examples.py's purpose is to illustrate uses of the montecarlo library.
    """

    print("Implementation of Completely Fictitious Casino!")
    print("1.   Coin Flips!")
    option = int(input("Choice: "))

    if (option == 1):
        x = coin.Coin()

        print(x.is_heads("H"))
        print(x.is_heads("HELLO"))
        pass

    else:
        exit()

if __name__ == "__main__":
    main()
