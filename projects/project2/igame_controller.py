# File: igame_controller.py

# Imports
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from projects.project2.cell import Cell
from projects.project2.grid import Grid
from datastructures.array2d import Array2D

# Implementation

T = TypeVar('T', bound=Any)

class IGameController(Generic[T], ABC):
    
    @abstractmethod
    def __init__(self, grid:Grid, rows:int, cols:int, secs:int) -> None:
        """Constructor method for the GameController class.
        Args:
            grid (Grid): the starting grid for the game.
            rows (int): the umber of rows in the grid.
            cols (int): the number of columns in the grid.
            secs (int): the number of seconds to pause between advancements in auto mode.
        Returns:
            None
        """
        ...

    @abstractmethod
    def run(self) -> None:
        """Method with the main loop to run the main Game of Life game.
        Args:
            None
        Returns:
            None
        """
        ...
               
    @abstractmethod 
    def advance_generation(self) -> None:
        """Method to advance the grid by one generation. Displays the grid.
        Args:
            None
        Returns:
            None
        """
        ...

    @abstractmethod
    def check_end(self) -> bool:
        """Method to check if the game has ended.
        Args:
            None
        Returns:
            bool: True if the game is still running, False otherwise.
        """
        ...
