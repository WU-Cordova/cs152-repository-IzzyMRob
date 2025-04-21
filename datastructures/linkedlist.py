# File: linkedlist.py

# Imports
from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T

# Implementation
# LinkedList Class
class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self._data_type: type = data_type
        self._count: int = 0
        self.head: LinkedList.Node | None = None
        self.tail: LinkedList.Node | None = None

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        if not isinstance(sequence, Sequence):
            raise TypeError("sequence must be of type Sequence.")
        linked_list: LinkedList[T] = LinkedList(data_type)
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError("All items in the sequence must be the same type.")
            linked_list.append(item)
        return linked_list

    def append(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("item must be of type data_type")
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        if self.empty:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("item must be of type data_type")
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        if self.empty:
            self.head = self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self._count += 1

    def insert_before(self, target: T, item: T) -> None:
        if self.empty:
            raise IndexError("LinkedList is empty")
        if not isinstance(target, self._data_type):
            raise TypeError("Target must be the same type as the rest of the LinkedList")
        if not isinstance(item, self._data_type):
            raise TypeError("Item must be the same type as the rest of the LinkedList")
        if not target in self:
            raise ValueError("Target not found in LinkedList")
        # search until current is target
        current = self.head
        while current != None:
            if current.data == target:
                break
            current = current.next
        # insert before
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        new_node.previous = current.previous # D <- O
        current.previous.next = new_node # D -> O
        current.previous = new_node # O <- G
        new_node.next = current # O -> G
        self._count += 1

    def insert_after(self, target: T, item: T) -> None:
        if self.empty:
            raise IndexError("LinkedList is empty")
        if not isinstance(target, self._data_type):
            raise TypeError("Target must be the same type as the rest of the LinkedList")
        if not isinstance(item, self._data_type):
            raise TypeError("Item must be the same type as the rest of the LinkedList")
        if not target in self:
            raise ValueError("Target not found in LinkedList")
        # search until current is target
        current = self.head
        while current != None:
            if current.data == target:
                break
            current = current.next
        # insert after
        new_node: LinkedList.Node = LinkedList.Node(data=item)
        new_node.next = current.next
        current.next.previous = new_node
        current.next = new_node
        new_node.previous = current
        self._count += 1

    def remove(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("item must be of type data_type")
        if self.empty:
            raise IndexError("Cannot remove when the LinkedList is empty")
        if not item in self:
            raise ValueError("Cannot remove item not in LinkedList")
        self.travel_node = self.head
        running = True
        while running:
            if self.travel_node.data == item:
                self.travel_node.previous.next = self.travel_node.next
                self.travel_node.next.previous = self.travel_node.previous
                self._count -= 1
                running = False
            self.travel_node = self.travel_node.next

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("item must be of type data_type")
        if self.empty:
            raise IndexError("Cannot remove when the LinkedList is empty")
        if not item in self:
            raise ValueError("Cannot remove item not in LinkedList")
        while self.head.data == item:
            self.pop_front()
        while self.tail.data == item:
            self.pop()
        self.travel_node = self.head
        while self.travel_node is not None:
            if self.travel_node.data == item:
                self.travel_node.previous.next = self.travel_node.next
                self.travel_node.next.previous = self.travel_node.previous
                self._count -= 1
            self.travel_node = self.travel_node.next
                    #remove

    def pop(self) -> T:
        if self.empty:
            raise IndexError("Cannot pop when LinkedList is empty.")
        data = self.tail.data
        if len(self) == 1: # head and tail are the same Node
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self._count -= 1
        return data
        
    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("Cannot pop when LinkedList is empty.")
        data = self.head.data
        if len(self) == 1: # head and tail are the same Node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self._count -= 1
        return data
    
    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError("LinkedList is empty.")
        return self.head.data

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError("LinkedList is empty.")
        return self.tail.data

    @property
    def empty(self) -> bool:
        if self.head == self.tail == None:
            return True
        return False

    def __len__(self) -> int:
        return self._count

    def clear(self) -> None:
        self._count = 0
        self.head = None
        self.tail = None

    def __contains__(self, item: T) -> bool:
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
          
    def __reversed__(self) -> ILinkedList[T]:
        new = LinkedList()
        for i in range(len(self)):
            new.append(self.pop())
        return new
    
    def __eq__(self, other: object) -> bool:
        self_copy = deepcopy(self)
        other_copy = deepcopy(other)
        for i in range(len(self_copy)):
            if self_copy.pop() != other_copy.pop():
                return False
            return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self._count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
