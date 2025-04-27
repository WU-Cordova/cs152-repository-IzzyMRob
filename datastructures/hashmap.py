import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
import math

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT,VT]]] = \
            Array(
                starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)],
                data_type=LinkedList
            )
        self._count: int = 0
        self._load_factor_threshold: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_index(self, key: KT, num_buckets: int) -> int:
        hash_result = self._hash_function(key)
        return hash_result % num_buckets

    def __getitem__(self, key: KT) -> VT:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k,v) in bucket_chain:
            if k == key:
                return v
        raise KeyError("Key is not in HashMap")

    def __setitem__(self, key: KT, value: VT) -> None:
        # get index and linked list of bucket
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        # loop through nodes, when key is correct set it to the new value and remove the old node
        for node in bucket_chain:
            if node[0] == key:
                bucket_chain.replace(node, (key,value))
                return #exit
        # if the key wasn't in the LinkedList add it
        bucket_chain.append((key,value))
        self._count += 1
        # handle resizing
        if self._count / len(self._buckets) > self._load_factor_threshold:
            self._resize()

    def keys(self) -> Iterator[KT]:
        keys = []
        for bucket in self._buckets:
            for node in bucket:
                keys.append(node[0])
        return iter(keys)
    
    def values(self) -> Iterator[VT]:
        values = []
        for bucket in self._buckets:
            for node in bucket:
                values.append(node[1])
        return iter(values)
    
    def items(self) -> Iterator[Tuple[KT, VT]]:
        items = []
        for bucket in self._buckets:
            for node in bucket:
                items.append(node)
        return iter(items)
                
    def __delitem__(self, key: KT) -> None:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k,v) in bucket_chain:
            if k == key:
                bucket_chain.remove((k,v))
                self._count -= 1
                return
        raise KeyError("Key is not in HashMap")

    def __contains__(self, key: KT) -> bool:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k,v) in bucket_chain:
            if k == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for node in bucket:
                yield node[0]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            raise TypeError("Other must ba a HashMap")
        if self.items == other.items and self.items == other.items:
            return True
        return False

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self._buckets) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"
    
    def _resize(self) -> None:
        """Method to increase the size of the HashMap."""
        old_buckets = self._buckets
        new_len = get_next_prime(len(old_buckets))
        self._buckets: Array[LinkedList[Tuple[KT,VT]]] = \
            Array(
                starting_sequence=[LinkedList(data_type=tuple) for _ in range(new_len)],
                data_type=LinkedList
            )
        for old_bucket in old_buckets:
            for old_node in old_bucket:
                new_index = self._get_bucket_index(old_node[0], new_len)
                new_chain = self._buckets[new_index]
                new_chain.append(old_node)

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)
    
def get_next_prime(current) -> int:
    """Returns the next prime number larger than double the number passed in."""
    def is_prime(n):
        """Returns True if the number is a prime, False otherwise"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n) + 1), 6): 
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def next_prime(N):
        """Returns the next prime number larger than N"""
        if N <= 1:
            return 2
        prime = N
        found = False
        while not found:
            prime += 1
            if is_prime(prime):
                found = True
        return prime
    
    return next_prime(current * 2)