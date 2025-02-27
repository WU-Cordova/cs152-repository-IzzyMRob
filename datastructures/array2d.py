from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from copy import deepcopy


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            # variables
            self.__row_index: int = row_index
            self.__array: IArray = array
            self.__num_columns: int = num_columns
            self.__data_type: type = data_type

        def __getitem__(self, column_index: int) -> T:
            # error for index out of bounds
            if column_index >= self.__num_columns:
                raise IndexError("Column index is out of bounds.")
            # return correct item
            return self.__array[self.map_index(self.__row_index, column_index)]
        
        def map_index(self, row_index: int, col_index: int) -> int:
            # calculate flat index from 2D coords
            return (row_index * self.__num_columns) + col_index
        
        def __setitem__(self, column_index: int, value: T) -> None:
            # set object at certain index to value
            self.__array[self.map_index(self.__row_index, column_index)] = value
        
        def __iter__(self) -> Iterator[T]:
            # start - column 0 for this row
            # stop - last column for this
            start = self.map_index(self.__row_index, 0)
            stop = self.map_index(self.__row_index, self.__num_columns)
            single_row: list = [deepcopy(self.__array[index]) for index in range(start, stop)]
            for item in single_row:
                yield item
        
        def __reversed__(self) -> Iterator[T]:
            # last and first value in the row
            start = self.map_index(self.__row_index, self.__num_columns)
            stop = self.map_index(self.__row_index, 0)
            single_row: list = [self.__array[index] for index in range(start, stop)]
            for item in single_row:
                yield item

        def __len__(self) -> int:
            return self.__num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.__num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.__row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.__num_columns - 1)])}, {str(self[self.__num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:        
        # raise errors
        if not isinstance(starting_sequence, Sequence): # starting_sequence must be a sequence
            raise ValueError("starting_sequence must be a sequence.")
        for row in starting_sequence:
            if not isinstance(row, Sequence): # each row must be a sequence
                raise ValueError("All rows in starting_sequence must be a sequence.")
            if len(row) != len(starting_sequence[0]): # each row must have the same length
                raise ValueError("All rows must be the same length.")
            for item in row:
                if not isinstance(item, data_type): # each item must be the same type
                    raise ValueError("All items in starting_sequence must be the same type.")
        
        # variables
        self.__data_type: type = data_type
        self.__num_rows: int = len(starting_sequence)
        self.__num_cols: int = len(starting_sequence[0])

        flat_starting_sequence: list = []
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                flat_starting_sequence.append(starting_sequence[row][col])

        self.__elements2d: Array = Array(flat_starting_sequence, self.__data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence: list = []
        for row in range(rows):
            starting_sequence.append([])
            for col in range(cols):
                starting_sequence[row].append(data_type())
        return Array2D(starting_sequence, data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return Array2D.Row(row_index, self.__elements2d, self.__num_cols, self.__data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]:
        # array[row] yields a row object
        # Row[col] yields the final value in the row
        rows: list = [self.Row(row_index, self.__elements2d, self.__num_cols, self.__data_type) for row_index in range(self.__num_rows)]
        for row in rows:
            yield row
   
    def __reversed__(self):
        rows: list = [self.Row(row_index, self.__elements2d, self.__num_cols, self.__data_type) for row_index in range(self.__num_rows)]
        rows.reverse()
        for row in rows:
            yield row
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_cols} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')