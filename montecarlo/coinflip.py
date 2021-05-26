#!/bin/env python3
# Coin flips!

# Imports
from games import coin
from edge import event

def coinflip():
    # 1: Our sample space
    sample_space = { "H", "T" }

    # 2: Our coin
    c = coin.Coin(sample_space)

    # 3: Get results for our coin
    # Output should be empty
    print(c.get_results())

    # 4: Get our sample space
    #print(c.get_sample_space())

    # 5: Access all possible outcomes (events)
    for i in event.event_space(sample_space):
        print(str(i) + "\t", end = '')
        # 6: Print probability of each event
        print(event.p_event(i, sample_space))
