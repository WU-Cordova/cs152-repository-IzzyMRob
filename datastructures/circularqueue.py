from copy import deepcopy
from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type:type=object) -> None:
        if not isinstance(maxsize, int):
            raise TypeError("maxsize must be an integer")
        if not isinstance(data_type, type):
            raise TypeError("data_type must me a type")
        #empty list for Array, 
        array = [data_type()] * (maxsize + 1)
        self._default = array[0]
        self._queue = Array(starting_sequence=array, data_type=data_type)
        self._max_size = maxsize
        self._data_type = data_type
        self._f = 0 #index of front element, left-most
        self._r = 0 #index past rear element, always empty, right-most
        self._length = 0

    def enqueue(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item must be the same type as the queue.")
        if self.full:
            return IndexError("Cannot enqueue when the queue is full.")
        self._queue[self._r] = item
        self._r += 1
        if self._r > self._max_size:
            self._r -= self._max_size
        self._length += 1

    def dequeue(self) -> T:
        if self.empty:
            raise IndexError("Cannot dequeue when queue is empty")
        front = self._queue[self._f]
        self._queue[self._f] = self._default
        self._f += 1
        if self._f > self._max_size:
            self._f -= self._max_size
        self._length -= 1
        return front

    def clear(self) -> None:
        array = [self._data_type()] * self._max_size
        self._queue = Array(starting_sequence=array, data_type=self._data_type)
        self._f = 0
        self._r = 0
        self._length = 0

    @property
    def front(self) -> T:
        return self._queue[self._f]
    
    @property
    def back(self) -> T:
        return self._queue[(self._r -1)]

    @property
    def full(self) -> bool:
        return self._length == self._max_size

    @property
    def empty(self) -> bool:
        return self._length == 0
    
    @property
    def maxsize(self) -> int:
        return self._max_size
    
    @property
    def datatype(self) -> type:
        return self._data_type

    def __eq__(self, other: object) -> bool:
        #handle wrong type
        if not isinstance(other, CircularQueue):
            raise TypeError("Both items must be Queues")
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        #diff lengths, diff front, diff back, diff data type
        if not len(self) == len(other):
            return False
        if not self.front == other.front:
            return False
        #if not self.back == other.back:
        #    return False
        if not self.datatype == other.datatype:
            return False
        for i in range(len(self_copy)):
            if self_copy.dequeue() != other_copy.dequeue():
                return False
        return True
        
    
    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, self._data_type):
            raise TypeError("item must be the same type as the rest of the queue.")
        if item in self._queue:
            return True
        else:
            return False
        
    def __getitem__(self, index: int) -> T:
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index >= len(self):
            raise IndexError("Index if out of range")
        return self._queue[index]
    
    def __len__(self) -> int:
        return self._length

    def __str__(self) -> str:
        return str(self._queue)

    def __repr__(self) -> str:
        return f'ArrayQueue({repr(self._queue)}), data type({self._data_type}), max size({self._max_size})'
                                  
