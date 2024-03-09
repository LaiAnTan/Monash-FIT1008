from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from generic_stack import Stack, T
from assets.ref_array import ArrayR


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

    def is_full(self) -> bool:
        """
        Returns True if the ArrayStack is full.

        :Complexity: O(1)
        """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """
        Clears the stack.

        :Complexity: O(1)
        """
        self.length = 0