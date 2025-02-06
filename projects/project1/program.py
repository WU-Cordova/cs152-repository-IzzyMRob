# File: program.py

# Imports (run as a debug to import properly)
from projects.project1.game import Game
import random

# Implimentation

def main():
    """Main function to run the Black Jack game."""    
    # loop to restart
    running = True
    while running:
        num_decks = (random.randint(1, 4)) * 2
        game = Game(num_decks)
        running = game.start_game()



if __name__ == '__main__':
    main()
