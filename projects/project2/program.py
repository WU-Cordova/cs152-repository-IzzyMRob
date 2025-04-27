# File: program.py

# Imports
from projects.project2.kbhit import KBHit
from projects.project2.cell import Cell, test_cell_string_repr
from projects.project2.grid import Grid
from projects.project2.game_controller import GameController
import random

"""
Main file to run the Game of Life.
-----
- To change the size of the grid change the values of ROWS and COLS below.
- To generate a random starting configuration set RANDOM_GRID = True.
- AUTO__PAUSE corresponds to the number of seconds the program will wait between
printing grids in automatic mode.
- To generate a random size of grid set RANDOM_SIZE = True. ROWS and COLS 
do not need to be changed.
- To input a specific sequence set RANDOM_GRID = False and enter the file
when prompted. Input files must be in the following format:
 -----------
|---X-      |  <-- grid representation
|XX---      |  <-- "-" means empty cell, "X" means filled cell
|-XX-X      |
 -----------
"""

ROWS = 3
COLS = 3
AUTO_PAUSE = 1
RANDOM_SIZE = False
RANDOM_GRID = True

# Implementation
def main(ROWS, COLS):
    if RANDOM_SIZE:
        ROWS = random.randint(10, 25)
        COLS = random.randint(10, 25)
    grid = Grid(ROWS, COLS, RANDOM_GRID)
    game_controller = GameController(grid, ROWS, COLS, AUTO_PAUSE)
    game_controller.run()


if __name__ == '__main__':
    main(ROWS, COLS)
    #test_cell_string_repr()