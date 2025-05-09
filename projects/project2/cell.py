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
        self._alive: bool = alive

    @property
    def alive(self) -> bool:
        return 
    
    
    @alive.setter
    def alive(self, value:bool) -> None:
        self._alive = value
    
    def next_state(self, count:int) -> bool:
        # 0 or 1 -> dead
        if count <= 1:
            return False
        # 2 -> no change
        elif count == 2:
            if self._alive:
                return True
            else:
                return False
        # 3 -> alive
        elif count == 3:
            return True
        # 4+ -> dead
        elif count >= 4:
            return False

    def __str__(self) -> str:
        if self._alive:
            return 'X'
        else:
            return " "
        
    def __repr__(self) -> str:
        return f"row: {self.row_pos}, col: {self.col_pos}, alive: {self._alive}"
        
    def tolist(self):
        return self
    
# tests for Cell class
def test_cell_string_repr(): #PASSED
    cell1 = Cell(3, 4, True)
    cell2 = Cell(0, 5, False)
    print(f"cell 1 str: {str(cell1)}")
    print(f"cell 1 repr: {repr(cell1)}")
    print(f"cell 2 str: {str(cell2)}")
    print(f"cell 2 repr: {repr(cell2)}")