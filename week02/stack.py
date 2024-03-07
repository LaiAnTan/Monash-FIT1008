from typing import TypeVar, Generic
from abc import ABC, abstractmethod

from assets.ref_array import ArrayR

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


class ArrayStack(Stack[T]):

    """
    Fixed-sized array implementation of Generic Stack ADT.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an ArrayStack of size max_capacity.

        :Complexity: O(max_capacity)
        """
        super().__init__()
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def is_full(self) -> bool:
        """
        Returns True if the ArrayStack is full.

        :Complexity: O(1)
        """
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        """
        Pushes an item onto the top of the stack.

        :Complexity: O(1)
        """

        if self.is_full():
            raise Exception("Stack is full")

        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """
        Pops an item off the top of the stack.

        :Complexity: O(1)
        """

        if self.is_empty():
            raise Exception("Stack is empty")

        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:

        """
        Peek at the item at the top of the stack.

        :Complexity: O(1)
        """

        if self.is_empty():
            raise Exception("Stack is empty")

        return self.array[self.length - 1]
