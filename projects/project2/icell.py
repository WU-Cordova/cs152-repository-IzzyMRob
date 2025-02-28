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
    def __str__(self) -> str:
        """Returns a string representation of the Cell.
        Returns: 
            A string representation of the Cell.
        """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """Returns a string representation of the Cell.
        Returns: 
            A string representation of the Cell.
        """
        ...