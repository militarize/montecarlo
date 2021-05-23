#!/bin/env python3
# examples.py
#       Predominantly used for illustrating modules and testing.
#
# Imports
from edge import event
from games import coin

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

if __name__ == '__main__':
    main()
