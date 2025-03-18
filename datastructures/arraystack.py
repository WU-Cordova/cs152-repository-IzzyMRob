# File: arraystack.py

# Imports
from copy import deepcopy
import os

from datastructures.array import Array, T
from datastructures.istack import IStack

# Implementation

# ArrayStack class
class ArrayStack(IStack[T]):
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        array = [data_type()] * max_size
        self._stack:list = Array(starting_sequence=array, data_type=data_type)
        self._max_size:int = max_size
        self._data_type:type = data_type
        self._top_index:int = -1 # index of the last object

    def push(self, item: T) -> None:
        #append stack, top index +1
        if not isinstance(item, self._data_type):
            raise TypeError("Item must be the same type as the Stack.")
        self._top_index += 1
        self._stack[self._top_index] = item

    def pop(self) -> T:
       #pop stack, top index -1
       #handle empty
       if self._top_index == -1:
            raise IndexError("Cannot pop when Stack is empty.")
       self._top_index -= 1
       self._stack.pop(self._top_index)

    def clear(self) -> None:
       #clear stack, top index = 0
       self._top_index = 0
       self._stack.clear()
    
    def peek(self) -> T:
       #return stack[top index]
       if self._top_index == -1:
           raise IndexError("Cannot peek when Stack is empty.")
       return self._stack[self._top_index]

    @property
    def maxsize(self) -> int:
        #return max size
        return self._max_size    
    
    @property
    def full(self) -> bool:
        # top index == len(stack) -1
        return self._top_index == len(self._stack) - 1

    @property
    def empty(self) -> bool:
        return self._top_index == -1
    
    def __eq__(self, other: object) -> bool:
        # not an Array, diff lengths, diff max sizes
        if not isinstance(other, ArrayStack):
            return False
        if len(self) != len(other):
            return False
        # copy, compare each element
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        for i in range(len(self)):
            if self_copy.pop() != other_copy.pop(): 
                return False
        return True
    

    def __len__(self) -> int:
       return self._top_index + 1
    
    def __contains__(self, item: T) -> bool:
       if not isinstance(item, self._data_type):
           raise TypeError("Item must be the same type as the Stack.")
       if item in self._stack:
           return True
       else:
           return False

    def __str__(self) -> str:
        return str([self._stack[i] for i in range(self._top_index + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self._max_size}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

