# File: program.py

# Imports (run as a debug to import properly)
from projects.project1.game import Game
import random

# Implimentation

def main():
    """Main function to play the Black Jack game."""    
    # loop to play multiple games
    running: bool = True
    while running:
        num_decks: int = (random.randint(1, 4)) * 2
        game: Game = Game(num_decks)
        running = game.start_game()



if __name__ == '__main__':
    main()
