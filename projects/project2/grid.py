# File: grid.py

# Imports
from projects.project2.igrid import IGrid, T
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from collections.abc import Sequence
import random

# Implementation

class Grid(IGrid[T]):

    def __init__(self, rows:int, cols:int, random_grid:bool, starting_sequence:bool=False):
        # raise errors
        # instance variables
        self.num_rows = rows
        self.num_cols = cols
        if random_grid:
            self.grid = self.create_random_grid()
        elif starting_sequence:
            self.grid = starting_sequence
        else:
            self.grid:Array2D = self.read_grid_file()


    def read_grid_file() -> Array2D:
        grid:list = []
        row:int = 0
        with open(input("Please input your starting file:")) as grid_file:
            finished:bool = False
            while not finished:
                line:str = grid_file.read_line().rstrip()
                if line is None:
                    finished = True
                else:
                    grid.append([])
                    col:int = 0
                    for char in line:
                        if char == "X":
                            grid[row].append(Cell(row, col, True))
                        elif char == "-":
                            grid[row].append(Cell(row, col, False))
                        col += 1
                    row += 1
        return grid
            
    def create_random_grid(self) -> Array2D:
        grid:list = []
        for row in range(self.num_rows):
            grid.append([])
            for col in range(self.num_cols):
                choice:bool = random.choice([True, False])
                grid[row].append(Cell(row, col, choice))
        return Array2D(grid, Cell)

    def display(self) -> None:
        print ("-" * ((self.num_cols *2)-1))
        for row in range(self.num_rows):
            row_list:list = []
            for col in range(self.num_cols):
                row_list.append(str(self.grid[row][col]))
            print("|".join(row_list))
            print ("-" * ((self.num_cols *2)-1))
        print(" ")

    def get_neighbors(self, c_row, c_col) -> int:
        #variable to store number of alive
        count:int = 0
        #loop through the 3x3 grid of cells around the current one
        for row in range(c_row-1, c_row+2):
            for col in range(c_col-1, c_col+2):
                if row >= 0 and col >= 0 and row < self.num_rows and col < self.num_cols: #row and col are not less than 0 or greater than max
                    if self.grid[row][col].alive:
                        count += 1
        #subtract 1 from count of the center cell was added above
        if self.grid[c_row][c_col].alive:
            count -= 1
        return count

    def next_generation(self) -> Array2D:
        # create new empty grid
        next_grid: list = []
        # count neighbors and apply rules to each cell
        for row in range(self.num_rows):
            next_grid.append([])
            for col in range(self.num_cols):
                num_neighbors:int = self.get_neighbors(row, col)
                next_state:bool = self.grid[row][col].next_state(num_neighbors)
                next_grid[row].append(Cell(row, col, next_state))
        return Array2D(next_grid)

    def __str__(self) -> str:
        return str(self.grid)
    
    def __repr__(self) -> str:
        return (f"rows: {self.num_rows}, cols: {self.num_cols}, grid: {self.grid}")

    def __eq__(self, value) -> bool:
        if isinstance(value, Grid) and self.num_rows == value.num_rows and self.num_cols == value.num_cols:
            return self.grid == value.grid
        return False