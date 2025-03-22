from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IQueue(Generic[T]):
    ''' Interface for a queue data structure '''

    @abstractmethod
    def __init__(self, maxsize: int = 0, data_type:type=object) -> None:
        """Initializes the CircularQueue object with a maxsize and data_type.
        Args:
            maxsize (int): The maximum size of the queue
            data_type (type): The type of the elements in the queue
        Returns:
            None
        Raises:
            TypeError:
                maxsize must be an integer
                data_type must be a type
        """
        ...

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Method to add an item to the back of the queue
        Args:
            item (T): The item to add to the queue
        Returns:
            None
        Raises:
            TypeError:
                item must be the same type as the rest of the queue
            IndexError:
                cannot enqueue when queue is full
        """
        ...

    @abstractmethod
    def dequeue(self) -> T:
        """Method to remove and return the item at the front of the queue
        Examples:
            >>> q = CircularQueue(maxsize=5, data_type=int)
            >>> q.enqueue(1)
            >>> q.enqueue(2)
            >>> q.enqueue(3)
            >>> q.dequeue()
            1
            >>> q.dequeue()
            2
            >>> q.dequeue()
            3
            >>> q.dequeue()
            IndexError('Queue is empty')
            >>> q.dequeue()
            IndexError('Queue is empty')
        Args:
            None
        Returns:
            T: The item at the front of the queue
        Raises:
            IndexError:
                If the queue is empty
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """Method to removes all items from the queue
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
    def front(self) -> T:
        """Method to see the first item in the queue without removing it
        Args:
            None
        Returns:
            T: The first item in the queue
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def back(self) -> T:
        """Method to see the last item in the queue without removing it
        Args:
            None
        Returns:
            T: The last item in the queue
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def full(self):
        """Method to check if the queue is full
        Args:
            None
        Returns:
            bool: True if the queue if full, False otherwise
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def empty(self) -> bool:
        """Method to check if the queue is empty
        Args:
            None
        Returns:
            bool: True if the queue if empty, False otherwise
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def maxsize(self):
        """Method to get the maximum size of the queue
        Args:
            None
        Returns:
            int: The max size of the queue
        Raises:
            None
        """
        ...

    @property
    @abstractmethod
    def datatype(self):
        """Method to get the data type of the queue
        Args:
            None
        Returns:
            type: The data type of the queue
        Raises:
            None
        """
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Returns True if this CircularQueue is equal to another object, False otherwise
        Equality is defined as:
            - The front and rear pointers are equal
            - The elements between the front and rear pointers are equal, even if they are in different positions
        Arguments:
            other: The object to compare this queue to
        Returns:
            bool: True if this queue is equal to another object, False otherwise
        Raises:
            TypeError:
                other must be a CircularQueue
        """
        ...

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """Method to check ot the queue contains an item
        Args:
            item (T): The item to check if in the queue
        Returns:
            bool: True if the item is in the queue, False otherwise
        Raises:
            TypeError:
                item must be the same type as the rest of the queue"""
        ...

    @abstractmethod
    def __getitem__(self, index:int) -> T:
        """Method to support bracket slicing of the queue
        Args:
            index (int): The index of the item ot get from the queue
        Returns:
            T: The item siced from the queue
        Raises:
            TypeError:
                index must be an integer
            ValueError:
                index must be less than the length of the queue
        """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """Method to get the length of the queue
        Args:
            None
        Returns:
            int: The number of items in the queue
        Raises:
            None
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Method to return a string representation of the queue
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
        """Method to return a detailed string representation of the queue
        Args:
            None
        Returns:
            str: detailed string representation of the stack
        Raises:
            None
        """
        ...


