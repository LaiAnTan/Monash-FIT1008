from __future__ import annotations

from generic_queue import Queue, T
from assets.ref_array import ArrayR


class LinearQueue(Queue[T]):

    """
    Fixed-sized Array implementation of Generic Queue ADT.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises a LinearQueue with a max capacity of max_capacity.

        :Complexity: O(max_capacity)
        """
        super().__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def append(self, item: T) -> None:
        """
        Appends an item to the end of the queue.

        :Complexity: O(1)
        """

        if self.is_full():
            raise Exception("Queue is full")
        
        self.array[self.rear] = item
        self.length += 1
        self.rear += 1

    def serve(self) -> T:
        """
        Serves an item from the front of the queue, deleting it and returning
        it from the front of the queue.

        :Complexity: O(1)
        """

        if self.is_empty():
            raise Exception("Queue is empty")
        
        self.length -= 1
        item = self.array[self.front]
        self.front += 1
        return item

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

    def is_full(self) -> bool:
        """
        Returns True if the queue is full.

        :Complexity: O(1)
        """

        return self.rear == len(self.array)

    def clear(self) -> None:
        """
        Removes all items from the queue.

        :Complexity: O(1)
        """
        super().__init__(self)
        self.front =  0
        self.rear = 0

    def resize(self) -> None:

        """
        Naive resize method implementation for a linear queue.

        Doubles the inner array's capacity when called.
        While copying, removes the unused space at the front of the array.

        :Complexity: O(n) * O(n * 2) = O(n^2) , where n is the length of the queue
        """

        new_array = ArrayR(len(self.array) * 2)

        i = 0

        for j in range(self.front, self.rear):

            new_array[i] = self.array[j]
            i += 1

        self.array = new_array
        self.front = 0
        self.rear = i + 1