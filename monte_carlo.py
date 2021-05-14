#!/bin/env python3
# Welcome to Monte Carlo!
# We offer coin flips, and not much else!
# Watch this space for more games.
# Will add elements of expectation.

# Imports
from monte_carlo import coin_flip
from monte_carlo import player

def main():
    print("Implementation of Completely Fictitious Casino!")
    print("Game?")
    print("1. Coin flip")
    print("2. Random")
    print("3: Player testing")    
    option = int(input("Choice: "))

    if (option == 1):
        number_of_games = int(input("How many times do you want play?: "))
        number_of_trials = int(input("Number of flips per game?: "))

        for n in range(number_of_games):
            game = coin_flip.CoinFlip()

            if (number_of_trials > 1):
                game.flip(number_of_trials)
                heads = game.get_heads()
                tails = game.get_tails()
                [fair, p, q] = game.coin_info()

                print("Game #: " + str(n+1) + "\tTotal flips: " + 
                    str(number_of_trials))
                print("success: " + str(p) + "\tfailure: " + str(q))
                print("# of heads: " + str(heads))
                print("# of tails: " + str(tails))
            else:
                print(game.flip())

    elif (option == 2):
        # This really is Bernoulli
        game = coin_flip.CoinFlip(False)
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
            game = coin_flip.CoinFlip(True)
            game.game(y)
            print(game.get_results())
            
            p = player.Player()
            p.post_results(game.get_results())
            p.get_results()

            players.append(p)

        print(players)
        
        for p in players:
            print(p.get_bankroll())
            print(p.get_results())

    else:
        exit()

if __name__ == "__main__":
    main()
