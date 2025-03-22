# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import deepcopy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        # raise errors
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence is not a valid sequence")
        if starting_sequence:
            if not isinstance(starting_sequence[0], data_type):
                raise TypeError("starting_sequence and data_type do not match")
        if not isinstance(data_type, type):
            raise ValueError("data_type is not a valid data type")

        # attributes
        self.__data_type = data_type
        self.__logical_size: int = len(starting_sequence) #number of elements
        self.__elements: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)
        self.__physical_size: int = len(self.__elements) #allocated storage
        
        # loop through all items in array and add all to elements
        for index, item in enumerate(deepcopy(starting_sequence)):
            # doesn't deep copy complex things because it refers back to og
            self.__elements[index] = deepcopy(item)

    @overload # multiple with same name, 
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        
        #returns
        if isinstance(index, int):
            if index >= len(self.__elements):
                raise IndexError("Index is out of range.")
            return self.__elements[index]
        elif isinstance(index, slice):
            return slice(self.__elements[index].tolist(), self.__data_type)
        else:
            raise TypeError("Index is not a slice or integer.")


    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"Item is not an instance of {self.__data_type}")

        self.__elements[index] = item

    def append(self, data: T) -> None:
        # grow storage in nessicary
        if self.__logical_size == self.__physical_size:
            self.__physical_size *= 2
        #save then empty elements
        elements = deepcopy(self.__elements)
        self.__elements: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)
        #re-add saved elements to elements and append new value
        self.__elements = np.append(arr = elements, values = data)
        self.__logical_size += 1
        self.__physical_size = len(self.__elements)

    def append_front(self, data: T) -> None:
        # grow storage in nessicary
        if self.__logical_size == self.__physical_size:
            self.__physical_size *= 2
        #save then empty elements
        elements = deepcopy(self.__elements)
        self.__elements: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)
        #append new value and re-add saved elements to elements 
        self.__elements = np.append(arr = data, values = elements)
        self.__logical_size += 1
        self.__physical_size = len(self.__elements)

    def pop(self) -> None:
        del self[self.__logical_size - 1]
    
    def pop_front(self) -> None:
        del self[0]
    
    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sequence):
            return False
        if len(self.__elements) != len(other):
            return False
        for index in range(0, len(self.__elements)):
            if not self.__elements[index] == other[index]:
                return False
        else:
            return True
    
    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements)

    def __reversed__(self) -> Iterator[T]:
        for i in range(self.__logical_size - 1,-1,-1):
            yield self.__elements[i]

    def __delitem__(self, index: int) -> None:
        if index >= len(self.__elements):
           raise IndexError("Index is out of range.")
        self.__elements = np.delete(self.__elements, index)
        self.__logical_size = self.__physical_size = len(self.__elements)

    def __contains__(self, item: Any) -> bool:
        if item in self.__elements:
            return True
        else:
            return False

    def clear(self) -> None:
        self.__elements = np.empty(0, dtype=object)
        self.__logical_size = 0
        self.__physical_size = 10

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self.__elements) + ']'
    
    def __repr__(self) -> str:
        return f'Array: {self.__str__()}, Logical: {self.__logical_size}, Physical: {self.__physical_size}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')