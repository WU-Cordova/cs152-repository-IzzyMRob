# File: program.py

# Imports
from projects.project2.kbhit import KBHit
from projects.project2.cell import Cell, test_cell_string_repr
from projects.project2.grid import Grid
from projects.project2.game_controller import GameController

"""
Main file to run the Game of Life.
-----
To change the size of the grid change the values of ROWS and COLS below.
To use a specific starting sequence assign it to STARTING_SEQUENCE and 
pass it into the grid creation below.
"""

ROWS = 10
COLS = 10
STARTING_SEQUENCE = None

# Implementation
def main():
    grid = Grid(ROWS, COLS)
    game_controller = GameController(grid)
    game_controller.run()


if __name__ == '__main__':
    main()
    #test_cell_string_repr()