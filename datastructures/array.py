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
        if not isinstance(starting_sequence, data_type):
            raise TypeError("starting_sequence and data_type do not match")
        if not isinstance(data_type, type):
            raise ValueError("data_type is not a valid data type")
        
        # attributes
        self.__elements: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)
        self.__physical_size: int = len(self.__elements)
        self.__logical_size: int = len(self.__elements)
        self.__data_type = data_type

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            return self.__elements[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        self.__elements = np.insert(self.__elements, index, item)

    def append(self, data: T) -> None:
        self.__elements = np.append(arr = self.__elements, values = data)

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        return self.__elements.size

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        raise

    def __delitem__(self, index: int) -> None:
       raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        raise NotImplementedError('Contains not implemented.')

    def clear(self) -> None:
        self.__elements = np.empty(0, dtype=self.__data_type)
        self.__logical_size = 0
        self.__physical_size = 10

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')