from __future__ import annotations

import sys
from pathlib import Path
from typing import Generic, TypeVar
from week02.stack.generic_stack import Stack

T = TypeVar('T')

# for path to import assets
sys.path.append(str(Path(__file__).resolve().parents[2]))


class Node(Generic[T]):

    def __init__(self, item: T = None) -> None:
        self.item = item
        self.next = None


class LinkedStack(Stack[T]):

    def __init__(self) -> None:
        """
        Initialises a linked stack ADT.

        :Complexity: O(1)
        """
        super().__init__()
        self.top = None

    def is_full(self) -> bool:
        """
        Returns True if the stack is full.

        :Complexity: O(1)
        """
        return False

    def clear(self) -> None:
        """
        Clears the stack.

        :Complexity: O(1)
        """
        super().clear()
        self.top = None

    def push(self, item: T) -> None:
        """
        Push an item onto the stack.

        :Complexity: O(1)
        """

        new = Node(item)

        new.next = self.top
        self.top = new
        self.length += 1

    def pop(self) -> T:
        """
        Pop an item off the stack.

        Complexity: O(1)
        """

        if self.is_empty() is True:
            raise ValueError("Stack is empty")

        item = self.top

        self.top = self.top.next
        self.length -= 1

        return item
