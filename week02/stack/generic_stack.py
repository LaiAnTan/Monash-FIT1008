from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')


class Stack(ABC, Generic[T]):

    """
    Abstract Base Class for Generic Stack ADT that contains type T
    """

    def __init__(self) -> None:
        """
        Initialises a generic stack.

        :Complexity: O(1)
        """

        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    def __len__(self) -> T:
        """
        Returns the length of the stack.

        :Complexity: O(1)
        """

        return self.length

    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty.

        :Complexity: O(1)
        """

        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        pass

    def clear(self) -> None:
        self.length = 0
