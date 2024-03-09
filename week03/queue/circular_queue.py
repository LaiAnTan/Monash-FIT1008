from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from generic_queue import Queue, T
from assets.ref_array import ArrayR


class CircularQueue(Queue[T]):

    """
    Fixed-sized Array implementation of Generic Queue ADT.
    An improved version of LinearQueue.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises a CircularQueue with a max capacity of max_capacity.

        :Complexity: O(max_capacity)
        """
        super().__init__()
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
        # wrap to front if necessary
        self.rear = (self.rear + 1) % len(self.array)

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
        # wrap to front if necessary
        self.front = (self.front + 1) % len(self.array) 
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

        return len(self) == len(self.array)

    def clear(self) -> None:
        """
        Removes all items from the queue.

        :Complexity: O(1)
        """
        super().__init__(self)
        self.front =  0
        self.rear = 0

    def __str__(self) -> str:
        """
        Returns the string representation of the queue.

        :Complexity: O(n) where n is the length of the queue.
        """

        index = self.front

        s = "["
        items = "" 

        for _ in range(len(self)):

            s += str(self.array[index]) + (", " if _ != len(self) - 1 else "")
            index = (index + 1) % len(self.array)

        return s + ']'
    
if __name__ == "__main__":

    q = CircularQueue(3)

    q.append(1)
    q.append(2)
    q.append(3)
    q.serve()
    q.append(5)

    print(f"Queue {q} is full? {q.is_full()}")