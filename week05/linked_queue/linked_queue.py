from __future__ import annotations

import sys
from pathlib import Path
from typing import Generic, TypeVar
from week03.queue.generic_queue import Queue

T = TypeVar('T')

# for path to import assets
sys.path.append(str(Path(__file__).resolve().parents[2]))


class Node(Generic[T]):

    def __init__(self, item: T = None) -> None:
        self.item = item
        self.next = None


class LinkedQueue(Queue[T]):

    def __init__(self) -> None:
        """
        Initialises a Linked Queue.

        :Complexity: O(1)
        """
        super().__init__()
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        """
        Returns True if the Queue is empty.

        :Complexity: O(1)
        """
        return self.front is None

    def is_full(self) -> bool:
        """
        Returns True if the Queue is full.

        :Complexity: O(1)
        """
        return False

    def append(self, item: T) -> None:
        """
        Appends item to the end of the Queue.

        :Complexity: O(1)
        """

        new = Node(item)

        if self.is_empty() is True:
            self.front = new
        else:
            self.rear.next = new
        self.rear = new # rear points to new no matter what
        self.length += 1

    def serve(self) -> T:
        """
        Serves an item from the front of the Queue.

        :Complexity: O(1)
        """

        if self.is_empty():
            raise ValueError("Queue is empty")

        item = self.front.item
        self.front = self.front.next
        self.length -= 1

        if self.is_empty():
            self.rear = None

        return item
