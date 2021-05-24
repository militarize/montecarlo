#!/bin/env python3
# examples.py
#       Predominantly used for illustrating modules and testing.
#
# Imports
from edge import event
from edge import freak
from games import coin

import numpy as np

def main():
    x = coin.Coin({"H", "T"})

    print(event.is_event({"H"}, x.get_sample_space()))

    events = set(tuple(e) for e in event.event_space({"H", "T"}))

    for e in events:
        print(e, end = '')
        print("\t\t\t", end = '')
        print(event.p_event(e, x.get_sample_space()))

    print()

    for c in event.combos(x.get_sample_space(), 3):
        print(c)

    x = np.random.randint(0, 6, 1000)

    print(freak.get_sample_space(x))

    print()
    print()

    probabilities = freak.p_event(x)
    
    print("The probabilities for all outcomes:")
    for p in probabilities:
        print(str(p) + ": " + str(probabilities[p]))
    print(sum(probabilities.values()))

if __name__ == '__main__':
    main()
