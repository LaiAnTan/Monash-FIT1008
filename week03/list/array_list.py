from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from generic_list import List, T
from assets.ref_array import ArrayR

class ArrayList(List[T]):

    """
    Fixed-sized array implementation of Generic List ADT.
    """

    MIN_CAPACITY = 1

    def __init__(self, initial_capacity: int) -> None:
        """
        Initialises an ArrayList.

        :Complexity: O(initial_capacity)
        """
        super().__init__()
        self.array = ArrayR(max(self.MIN_CAPACITY, initial_capacity))

    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at position index.

        :Complexity: O(1)
        """
        self.array[index] = item

    def __getitem__(self, index: int) -> T:
        """
        Gets the item stored at position index.

        :Complexity: O(1)
        """
        return self.array[index]
    
    def append(self, item: T) -> None:

        """
        Appends an item to the end of the list.

        :Complexity: O(n) where n is the length of the list
        """

        self.insert(len(self), item)


    def insert(self, index: int, item: T) -> None:

        """
        Insert an item at position index of the list.

        :Complexity: O(n) where n is the length of the list
        """

        if len(self) == len(self.array):

            new_array = ArrayR(self.__newsize())

            for i in range(len(self)):
                new_array[i] = self.array[i]

            self.array = new_array

        for i in range(len(self) - 1, index, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = item
        self.length += 1

    def delete(self, index: int) -> T:
        """
        Deletes and returns the item at position index.

        :Raises IndexError: if index is out of bounds
        :Complexity: O(n) where n in the size of the list
        """

        item = self.array[index]

        self.length -= 1

        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

        return item


    def index(self, item: T) -> int:
        """
        Look for an item's index in the list.

        :raise ValueError: if the item is not found
        :Complexity: O(n * comp) where n is the size of the list
        """

        for i in range(len(self)):
            if item == self.array[i]:
                return i
        
        raise ValueError("item not in list")

    def __newsize(self) -> int:
        """
        Python's formula for calculating list resizes, growing by approximately
        12% per resize.
        """
        return self.length + (self.length >> 3) + (3 if self.length < 9 else 6)

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
        Clears the list.

        :Complexity: O(1)
        """

        self.length = 0

    def __str__(self) -> str:
        """
        Returns the string representation of the list.

        :Complexity: O(n) where n is the length of the list.
        """

        s = "["

        for i in range(len(self)):

            s += str(self.array[i]) + (", " if i != len(self) - 1 else "")

        return s + ']'

if __name__ == "__main__":

    l = ArrayList(10)

    for i in range(11):
        l.append(i)

    print(len(l))
    print(len(l.array))
    print(l)

    l.insert(5, 199)
    print(l)


