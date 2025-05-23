from copy import deepcopy
import os
from datastructures.istack import IStack
from typing import Generic
from datastructures.linkedlist import LinkedList, T

class ListStack(Generic[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self._data_type = data_type
        self.stack = LinkedList(self._data_type)

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        self.stack.prepend(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        return self.stack.pop_front()

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if len(self) == 0:
            raise IndexError("Cannot peek when Stack is empty.")
        return self.stack.front

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.stack.empty

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.stack = LinkedList(self._data_type)

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        if item in self.stack:
            return True
        return False

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance(other, ListStack):
            return False
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        for i in range(len(self_copy)):
            if self_copy.pop() != other_copy.pop():
                return False
            return True

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.stack)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self.stack)

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        return repr(self.stack)
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
