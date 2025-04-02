# File: linkedlist.py

# Imports
from __future__ import annotations
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
        self._data_type = data_type
        self._count = 0
        self.head: LinkedList.Node | None = None
        self.tail: LinkedList.Node | None = None
        self._counter: int = 0

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
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

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

    def __iter__(self) -> ILinkedList[T]:
        return self

    def __next__(self) -> T:

          
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

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
