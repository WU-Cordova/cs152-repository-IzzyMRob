# File: igrid.py

# Imports
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from datastructures.array2d import Array2D
from collections.abc import Sequence

# Implementation

T = TypeVar('T', bound=Any)

class IGrid(Generic[T], ABC):

    @abstractmethod
    def __init__(self, starting_grid:Sequence):
        """Constructor method for the Grid class.
        Args:
            starting_grid (Array2D): a starting sequence to initialize the game
        Returns: 
            None
        Raises:
            ValueError: 
                
        """
        ...

    @abstractmethod
    def display(self) -> None: