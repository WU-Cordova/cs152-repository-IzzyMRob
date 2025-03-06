# File: grid.py

# Imports
from projects.project2.icell import ICell, T
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from collections.abc import Sequence
import random

# Implementation

class Grid(ICell[T]):

    def __init__(self, rows, cols, starting_grid:Sequence):
        # raise errors
        # instance variables
        self.num_rows = len(starting_grid)
        self.num_cols = len(starting_grid[0])
        if starting_grid:
            self.grid = starting_grid
        else:
            self.grid = self.create_random_grid()

    def create_random_grid(self) -> Array2D:
        grid = []
        for row in range(self.num_rows):
            grid.append([])
            for col in range(self.num_cols):
                choice = random.choice([True, False])
                grid[row].append(Cell(row, col, choice))
        return Array2D(grid, Cell)

    def display(self) -> None:
        print ("_" * (self.num_cols *2))
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print("|".join(self.grid[row][col]))
        print ("_" * (self.num_cols *2))


    def get_neighbors(self, c_row, c_col) -> int:
        #variable to store alive
        count = 0
        #loop through the 3x3 grid of cells around the current one
        for row in range(c_row-1, c_row+2):
            for col in range(c_col-1, c_col+2):
                if row >= 0 and col >= 0 and row <= self.num_rows and col <= self.num_cols: #row and col are not less than 0 or greater than max
                    if self.grid[row][col].alive:
                        count += 1
        #subtract 1 from count of the center cell was added above
        if self.grid[c_row][c_col].alive:
            count -= 1
        return count

    def next_generation(self) -> Grid:
        # create new grid
        next_grid:Grid = Grid(self.num_rows, self.num_cols)
        # count neighbors and apply rules to each cell
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                num_neighbors:int = self.get_neighbors(row, col)
                next_state:bool = self.grid[row][col].next_state(num_neighbors)
                next_grid[row][col] = Cell(row, col, next_state)
        return next_grid

    def __str__(self):
        for row in self.grid:
            print

    def __eq__(self, value):
        if isinstance(value, Grid) and self.rows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False


test_grid = [[Cell()]]

def test_display():
    grid = Grid(3, 4, )