# File: game.py

from projects.project1.multideck import MultiDeck

class Game:

    def __init__(self):
        pass

    
    def start_game(self) -> None:
        """ Starts the game. Algorithm: 
            1. While no score is above 21, do the following:
                1.1. Allow Player to Hit or Stay.
                1.2. If Player busts, break the loop.
                1.3. When Player Stays dealer takes their turn.
            2. Print the result of the battle.
        """
        game_over = False
        while game_over == False:
            if not game_over:
                game_over = self.attack(self.p1, self.p2)
            if not game_over:
                game_over = self.attack(self.p2, self.p1)