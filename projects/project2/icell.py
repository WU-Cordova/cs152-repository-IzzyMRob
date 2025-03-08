# File: icell.py

# Imports
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

# Implementation

T = TypeVar('T', bound=Any)

class ICell(Generic[T], ABC):
    
    @abstractmethod
    def __init__(self, row:int, col:int, alive:bool) -> None:
        """Constructor function for the Cell class.
        Args: 
            row (int): row position of the Cell
            col (int): column position of the Cell
            alive (bool): is the Cell alive
        Returns:
            None
        Raises:
            ValueError:
                row and col must be integers,
                alive must be a boolean
        """
        ...

    @abstractmethod 
    def next_state(self, count:int) -> bool:
        """Method to determine if the Cell will ba alive or not in the next generation.
        Args:
            count (int): the number of alive neighbors the Cell has.
        Returns:
            bool: True of the Cell will be alive next generation, False otherwise.
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Method to return a string representation of the Cell.
        Args:
            None
        Returns:
            str: 'X' if the Cell is alive, '-' otherwise.
        """
        ...
        
    @abstractmethod
    def __repr__(self) -> str:
        """Method to return a detailed string representation of the Cell.
        Args:
            None
        Returns:
            str: Contains info about the number of rows, columns, and alive state.
        """
        ...
        
    @abstractmethod
    def tolist(self):
        """Method to turn the Cell into a list.
        Args:
            None
        Returns:
            self
        """
        ...
