#!/bin/env python3
# Coin flips!

# Imports
from games import coin
import event


def coinflip():
    # 1: Our sample space
    sample_space = { "H", "T" }

    # 2: Our coin
    c = coin.Coin(sample_space)

    # 3: event A
    A = { "H" }

    # 4: P(A)
    print(event.P(A, sample_space))

    # 5: P(sample_space)
    print(event.P(sample_space, sample_space, frac = True))

    # 6: let B = NOT(A)
    B = event.NOT(A, sample_space)
    print(event.P(B, sample_space, frac = True))

    # 7: List all subsets of sample_space
    for i in event.powerset(sample_space):
        print(i)

    # 8: A OR B
    print(event.P((A | B), sample_space))
    print(event.P(event.AND(A, B), sample_space))
    print(event.P(A.intersection(B), sample_space))


    # 9: Biased coin
    c = coin.Coin({ "H": 2, "T": 1 })
    print(c.get_sample_space())
    print(event.P({"H"}, c.get_sample_space()))
    for i in event.powerset(sample_space):
        print(i)

def main():
    # Coin flips
    coinflip()

main()
