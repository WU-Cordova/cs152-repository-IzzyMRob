# File: istack.py

# Imports
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Implementation

T = TypeVar('T')

# IStack class
class IStack(Generic[T], ABC):
    """ ArrayStack class that implements the interface from IStack. 
        The ArrayStack is a fixed-size stack that uses an Array to store the items."""

    @abstractmethod
    def __init__(self, max_size:int = 0, data_type=object) -> None:
        """Constructor to initialize the ArrayStack object
        Args: 
            max_size (int): The maximum size of the stack. 
            data_type (type): The data type of the stack.
        Returns:
            None
        Raises:
            TypeError:
                max_size must be an integer
                data_type must be a type
        """
        ...

    @abstractmethod
    def push(self, item: T) -> None:
        """Method to add an item to the top of the stack
        Args:
            item (type): The item to add to the stack
        Returns:
            None
        Raises:
            TypeError:
                item must be of type data_type
            IndexError:
                stack cannot be full
        """
        ...

    @abstractmethod
    def pop(self) -> T:
        """Method to remove an item from the top of the stack
        Args:
            None
        Returns:
            T: the top object of the stack
        Raises:
            IndexError:
                Cannot pop when stack is empty
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """Method to empty the contents of the stack
        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def peek(self) -> T:
        """Method to look at the item on top of the Stack without removing it
        Args:
            None
        Returns:
            T: the top object of the stack
        Raises:
            IndexError:
                Cannot pop when stack is empty
        """
        ...

    @property
    @abstractmethod
    def empty(self) -> bool:
        """Method to check if the Stack is empty
        Args:
            None
        Returns:
            bool: True of the stack is empty, False otherwise
        Raises:
            None
        """
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Method to check if two stacks are equal to each other. Checks for equal max_size and elements
        Args:
            other (ArrayStack): the stack to compare to
        Returns:
            bool: True of the stacks are the same, False otherwise
        Raises:
            TypeError:
                other must be a ArrayStack
        """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """Method to find the length of the stack. 
        Args:
            None
        Returns:
            int: the number of elements in the stack
        Raises:
            None
        """
        ...
    
    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """Method to check if an item is in the stack
        Args:
            None
        Returns:
            bool: True if the item is in the stack, False otherwise
        Raises:
            TypeError:
                item must be the same type as the rest of the stack
        """
        ...
    

    @abstractmethod
    def __str__(self) -> str:
        """Method to return a string representation of the stack
        Args:
            None
        Returns:
            str: string representation of the stack
        Raises:
            None
        """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """Method to return a detailed string representation of the stack
        Args:
            None
        Returns:
            str: detailed string representation of the stack
        Raises:
            None
        """
        ...