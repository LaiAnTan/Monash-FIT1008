from __future__ import annotations
from generic_sorted_list import SortedList, T
from assets.ref_array import ArrayR

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


class ArraySortedList(SortedList[T]):

    MIN_CAPACITY = 1

    def __init__(self, initial_capacity: int) -> None:
        """
        Initialises an ArraySortedList.

        :Complexity: O(initial_capacity)
        """
        super().__init__()
        self.array = ArrayR(max(self.MIN_CAPACITY, initial_capacity))

    def __getitem__(self, index: int) -> T:
        return self.array[index]

    def delete(self, index: int) -> T:

        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def index(self, item: T) -> int:
        """
        Wrapper because I want two versions of the index function for showcase
        purposes
        """
        return self.index_binary(item)

    def index_linear(self, item: T) -> int:
        """
        Look for an item's index in the list with linear search.

        :raise ValueError: if the item is not found
        :Complexity:
            let n be the number of elements in the list
            let m be the comparisons made in the function
            Best-case: O(m) when the item is in the first index
            Worst-case: O(n * m) when the item is in the last index
        """

        for i in range(len(self)):

            if item == self.array[i]:
                return i
            # stop early if item smaller than item in current position
            # in a sorted list the item will never be after items bigger than
            # it
            elif item < self.array[i]:
                break

        raise ValueError("Item not in list")

    def index_binary(self, item: T) -> int:
        """
        Look for an item's index in the list with binary search.

        :raise ValueError: if the item is not found
        :Complexity:
            let n be the number of elements in the list
            Best-case: O(1) when the item is in the middle
            Worst-case: O(log n) when the item is in the extrema
        """
        low = 0
        high = len(self) - 1

        while low <= high:

            mid = low + high // 2

            if self.array[mid] > item:
                high = mid - 1
            elif self.array[mid] == item:
                return mid
            else:
                low = mid + 1

        raise ValueError("Item not in list")

    def remove(self, item: T) -> None:
        index = self.index(item)
        self.delete(index)

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        self.length = 0

    def add(self, item: T) -> None:
        """
        Adds an item into the list, sorting it in the process.

        :Complexity: O(n) where n is the length of the list
        """
        index = self.__index_to_add(item)
        self.__make_space(index)
        self.array[index] = item
        self.length += 1

    def __make_space(self, index: int) -> None:
        """
        Makes space in the list at the current index.
        Resizes if required.
        """

        if len(self.array) == len(self):
            self.__resize()

        for i in range(len(self) - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = None

    def __newsize(self) -> int:
        """
        Python's formula for calculating list resizes, growing by approximately
        12% per resize.
        """
        return self.length + (self.length >> 3) + (3 if self.length < 9 else 6)

    def __resize(self) -> None:
        """
        Resizes the array to a new size using __newsize.
        """

        new_array = ArrayR(self.__newsize())

        for i in range(len(self)):
            new_array[i] = self.array[i]

        self.array = new_array

    def __index_to_add(self, item: T) -> int:
        """
        Look for an item's index in the list with binary search.

        :Complexity:
            let n be the number of iterations of the while loop
            let m be the
            Best-case: O(m) when the position item is in the middle
            Worst-case: O(m log n) when the position item is in the extrema
        """
        low = 0
        high = len(self) - 1

        while low <= high:

            mid = (low + high) // 2

            if self.array[mid] is None or self.array[mid] > item:
                high = mid - 1
            elif self.array[mid] is None or self.array[mid] < item:
                low = mid + 1
            else:
                return mid

        return low


if __name__ == "__main__":

    import random

    x = ArraySortedList(3)

    for i in range(20):
        num = random.randint(-50, 50)
        print(num)
        x.add(num)
        print(x.array)

    x.delete(2)
    print(x.array)
    x.delete(0)
    print(x.array)
