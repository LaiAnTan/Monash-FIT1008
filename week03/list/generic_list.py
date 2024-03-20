from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')


class List(ABC, Generic[T]):

    def __init__(self) -> None:
        """
        Initialises a Generic List.

        :Complexity: O(1)
        """
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass
    
    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def delete(self, index) -> T:
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        pass

    def remove(self, item: T) -> None:
        """
        Removes the first occurence of an item.

        :Complexity: O(delete)
        """

        index = self.index(item)
        self.delete(index)

    def __len__(self) -> int:
        """
        Returns the length of the list.

        :Complexity: O(1)
        """

        return self.length
    
    def is_empty(self) -> bool:
        """
        Returns True if the list is empty.

        :Complexity: O(1)
        """

        return len(self) == 0
    
    def clear(self):
        """
        Clears the stack.

        :Complexity: O(1)
        """

        self.length = 0
