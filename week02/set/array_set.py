from __future__ import annotations
from typing import TypeVar

from generic_set import Set, T
from assets.ref_array import ArrayR


class ArraySet(Set[T]):

    """
    Fixed-sized array implementation of Generic Set ADT.
    """

    MIN_CAPACIITY = 1

    def __init__(self, max_capacity) -> None:
        """
        Initialises an ArraySet of size max_capacity.

        :Complexity: O(max_capacity)
        """

        super().__init__()
        self.array = ArrayR(max(self.MIN_CAPACIITY, max_capacity))

    def clear(self) -> None:
        """
        Clears every element from the set.

        :Complexity: O(1)
        """

        self.size = 0

    def __len__(self) -> int:
        """
        Returns the size of the set.

        :Complexity: O(1)
        """

        return self.size

    def is_empty(self) -> bool:
        """
        Returns True if the set is empty.

        :Complexity: O(1)
        """

        return len(self) == 0

    def is_full(self) -> bool:
        """
        Returns True if the set is full.

        :Complexity: O(1)
        """

        return len(self) == len(self.array)

    def __contains__(self, item: T) -> bool:
        """
        Returns True if the set contains item.

        :Complexity: O(n * comparisons)
        """
        for i in range(self.size):

            if item == self.array[i]:
                return True

        return False

    def add(self, item: T) -> None:
        """
        Adds an item to the set.

        :Complexity: O(n * comparisons)
        """

        if self.is_full():
            raise Exception("Set is full")

        if item not in self:

            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        """
        Removes an item from the set.

        :Complexity: O(n * comparisons)
        """

        for i in range(self.size):
            if item == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                break
        else:
            raise KeyError(item)

    def union(self, other: Set[T]) -> Set[T]:
        """
        Computes the union of two sets.

        :Complexity: O(m * (n + m) * comparisons), where n and m are the sizes
        of self and other respectively.
        """

        res = ArraySet(len(self.array) + len(other.array))  # O(n + m)

        for i in range(len(self)):  # O(n)
            res.array[i] = self.array[i]

        res.size = self.size

        for j in range(len(other)):  # O(m)
            res.add(other.array[j])  # O((m + n) * comparisons)

        return res

    def intersection(self, other: Set[T]) -> Set[T]:
        """
        Computes the intersection of two sets.

        :Complexity: O((n * comparisons) * (m + n) * comparisons),
        where n and m are the sizes of self and other respectively.
        """

        res = ArraySet(len(self.array) + len(other.array))  # O(n + m)

        for i in range(len(self)):  # O(n)

            if self.array[i] in other:  # O(n * comparisons)
                res.add(self.array[i])  # O((m + n) * comparisons)

        return res

    def difference(self, other: Set[T]) -> Set[T]:
        """
        Computes the difference of two sets.

        :Complexity: O(m * (n + m) * comparisons), where n and m are the sizes
        of self and other respectively.
        """

        res = ArraySet(len(self.array) + len(other.array))  # O(n + m)

        for i in range(len(self)):  # O(n)

            if self.array[i] not in other:  # O(n * comparisons)
                res.add(self.array[i])  # O((m + n) * comparisons)

        return res
