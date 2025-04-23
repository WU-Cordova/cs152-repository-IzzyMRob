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
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k,v) in bucket_chain:
            if k == key:
                v = value
            else:
                bucket_chain.append((key, value))
        self._count += 1

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
        for bucket in self._buckets:
            if key in bucket:
                bucket.remove(key)
            else:
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
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self._buckets) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"
    
    def _resize(self) -> None:
        temp_buckets = self._buckets
        # find next doubled prime number
        # init new empty bucket list
        # move all items over

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

    def isPrime(n):
        
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5,int(math.sqrt(n) + 1), 6): 
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def nextPrime(N):
        if N <= 1:
            return 2
        prime = N
        found = False
        while not found:
            prime += 1
            if isPrime(prime):
                found = True
        return prime
    
    return nextPrime(current * 2)