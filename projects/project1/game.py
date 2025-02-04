# File: game.py

import random
#from projects.project1.multideck import MultiDeck

class Game:

    def __init__(self, num_decks):
        self._deck = MultiDeck(num_decks)

    
    def run(self) -> None:
        """ Starts the game. Algorithm: 
            1. While no score is above 21, do the following:
                1.1. Allow Player to Hit or Stay.
                1.2. If Player busts, break the loop.
                1.3. When Player Stays dealer takes their turn.
            2. Print the result of the battle.
        """
        running = True
        while running:
            num_decks = (random.randint[1, 4]) * 2
            print(num_decks)