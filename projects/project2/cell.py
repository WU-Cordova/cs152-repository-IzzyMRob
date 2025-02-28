# File: cell.py

# Imports
from projects.project2.icell import ICell, T

# Implementation

class Cell(ICell[T]):

    def __init__(self, row:int, col:int, alive:bool) -> None:
        # raise errors - wrong type passed in
        if not isinstance(row, int):
            raise ValueError("row must be an integer.")
        if not isinstance(col, int):
            raise ValueError("col must be an integer.")
        if not isinstance(alive, bool):
            raise ValueError("alive must be a boolean.")
        # instance variables
        self.row_pos: int = row
        self.col_pos: int = col
        self.alive: bool = alive

    def __str__(self) -> str:
        # X means the cell is filled with an alive Cell
        if self.alive:
            return "X"
        else:
            return " "
        
    def __repr__(self) -> str:
        return f"row: {self.row_pos}, col: {self.col_pos}, alive: {self.alive}"
        

# tests for Cell class
def test_cell_string_repr(): #PASSED
    cell1 = Cell(3, 4, True)
    cell2 = Cell(0, 5, False)
    print(f"cell 1 str: {str(cell1)}")
    print(f"cell 1 repr: {repr(cell1)}")
    print(f"cell 2 str: {str(cell2)}")
    print(f"cell 2 repr: {repr(cell2)}")