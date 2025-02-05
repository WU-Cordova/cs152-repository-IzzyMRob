# File: program.py

# Imports (run as a debug to import from datastructures properly)
from projects.project1.game import Game
import random

# Constants

# Implimentation

# card, deck and game classes
# create decks, shuffle and deal
# game play, dealer, score

def main():
    num_decks = (random.randint(1, 4)) * 2
    game = Game(num_decks)
    game.run()



if __name__ == '__main__':
    main()
