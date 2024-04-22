from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

K = TypeVar("K")
V = TypeVar("V")

class HashTable(ABC, Generic[K, V]):
    
    """
    Abstract Base Class for Generic Hash Table ADT that contains type T
    """
    
    def __init__(self) -> None:
        """
        Initialise the Hash Table.
        """
        self.count = 0
    
    @abstractmethod
    def hash(self, key: K) -> int:
        pass

    def __len__(self) -> int:
        """
        Returns the number of elements in the hash table.
        """
        return self.count
    
    @abstractmethod
    def keys(self) -> list[K]:
        pass
    
    @abstractmethod
    def values(self) -> list[V]:
        pass
    
    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True
    
    
    @abstractmethod
    def __delitem__(self, key: K) -> None:
        pass
    
    @abstractmethod
    def __setitem__(self, key: K, data: V) -> None:
        pass

    @abstractmethod
    def __getitem__(self, key: K) -> V:
        pass

    def is_empty(self) -> bool:
        return self.count == 0
