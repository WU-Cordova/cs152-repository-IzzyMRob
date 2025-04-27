# File: igrid.py

# Imports
from projects.project2.icell import ICell, T
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from collections.abc import Sequence
import random
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

# Implementation

class IGrid(ICell[T], ABC):

    @abstractmethod
    def __init__(self, rows:int, cols:int, random_grid:bool, starting_sequence:bool=False) -> None:
        """Constructor method for the Grid class.
        Args:
            rows (int): the number of rows in the grid
            cols (int): the number of columns in the grid
            random_grid (bool): True if a random grid should be created, False otherwise
            starting_sequence (bool): True if a starting file will be uploaded by the user, False otherwise
        Returns:
            None
        """
        ...

    @abstractmethod
    def read_grid_file() -> Array2D:
        """Method to read in a file from the user and turn it into an Array2D.
        Args:
            None
        Returns:
            Array2D: the starting grid to be used by the constructor method.
        """
        ...

    @abstractmethod
    def create_random_grid(self) -> Array2D:
        """Method to create a random grid.
        Args:
            None
        Returns:
            Array2D: the starting grid to be used by the constructor method.
        """
        ...
    
    @abstractmethod
    def display(self) -> None:
        """Method to create display the grid to the terminal.
        Args:
            None
        Returns:
            None
        """
        ...

    @abstractmethod
    def get_neighbors(self, c_row, c_col) -> int:
        """Method to count the number of alive neighbors to a single cell.
        Args:
            c_row (int): the row index of the cell to check
            c_col (int): the column index of the cell to check
        Returns:
            int: the number of alive neighbors
        """
        ...

    @abstractmethod
    def next_generation(self) -> Array2D:
        """Method to get the grid of the next generation.
        Args:
            None
        Returns:
            Array2D: The array of the next generation's grid
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Method to return the string representation of the Grid.
        Args:
            None
        Returns:
            str: the string representation of the grid
        """
        ...
    
    @abstractmethod
    def __repr__(self) -> str:
        """Method to return the detailed string representation of the Grid.
        Args:
            None
        Returns:
            str: the detailed string representation of the grid
        """
        ...

    @abstractmethod
    def __eq__(self, value) -> bool:
        """Method to determine if two grids are equal to each other.
        Args:
            value (Grid): The grid to compare to self
        Returns:
            bool: True of the grids are the same, False otherwise
        """
        ...
        