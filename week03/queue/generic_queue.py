from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')


class Queue(ABC, Generic[T]):

    """
    Abstract Base Class for Generic Queue ADT that contains type T
    """

    def __init__(self) -> None:
        """
        Initialises a generic queue.

        :Complexity: O(1)
        """

        self.length = 0

    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def serve(self) -> T:
        pass

    def __len__(self) -> T:
        """
        Returns the length of the queue.

        :Complexity: O(1)
        """

        return self.length

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty.

        :Complexity: O(1)
        """

        return len(self) == 0


    @abstractmethod
    def is_full(self) -> bool:
        pass

    def clear(self) -> None:
        """
        Removes all items from the queue.

        :Complexity: O(1)
        """
        self.length = 0
