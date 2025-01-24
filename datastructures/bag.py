from typing import Iterable, Optional
from datastructures.ibag import IBag, T

# dictionary - item is key, count is value
# list - unique items in the outer list, count in inner

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        # create main dictionary of type T and integers
        self.__bag: dict[T, int] = {}
        
        # add items if they were passed in
        if items:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        # if already in bag increase count, if not add it
        if item == None:
            raise TypeError("Cannot add None type")
        elif item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1

    def remove(self, item: T) -> None:
        # if it's in the bag and there is at least one of them
        if item in self.__bag and self.__bag[item] > 0:
            self.__bag[item] -= 1
        else:
            print(f"There is no {item} in the bag!")

    def count(self, item: T) -> int:
        # if it's in the bag return the value/count
        if item in self.__bag:
            return self.__bag[item]
        else:
            return 0

    def __len__(self) -> int:
        # start total as 0
        total = 0
        
        # for every item add how many of it there are
        for item in self.__bag:
            total += self.__bag[item] 
        return total

    def distinct_items(self) -> Iterable[T]:
        # blank list
        items: list[T] = []
        
        # add every key in the bag
        for item in self.__bag:
            items.append(item)
        return items
    
    def __contains__(self, item) -> bool:
        # return true if item is on the bag, false otherwise
        if item in self.__bag:
            return True
        else:
            return False

    def clear(self) -> None:
        # same code is init, resets the dictionary
        self.__bag: dict[T, int] = {}