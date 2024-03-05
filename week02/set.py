from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

from ref_array import ArrayR

T = TypeVar('T')


class Set(ABC, Generic[T]):

    """
    Abstract Base Class for Generic Set ADT that contains type T
    """

    def __init__(self) -> None:
        self.clear()

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        pass

    @abstractmethod
    def union(self, other: Set[T]) -> Set[T]:
        pass

    @abstractmethod
    def intersection(self, other: Set[T]) -> Set[T]:
        pass

    @abstractmethod
    def difference(self, other: Set[T]) -> Set[T]:
        pass


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


class BVSet(Set[T]):

    """
    Bit Vector implementation of Set ADT.
    """

    MIN_CAPACIITY = 1

    def __init__(self) -> None:
        """
        Initialises an BVSet.

        :Complexity: O(1)
        """

        super().__init__()

    def clear(self) -> None:
        """
        Clears every element from the set.

        :Complexity: O(1)
        """

        self.elems = 0

    def __len__(self) -> int:
        """
        Returns the size of the set.

        :Complexity: O(|elems|)
        """

        size = 0
        for item in range(1, self.elems.bit_length() + 1):
            if item in self:
                size += 1

        return size

    def is_empty(self) -> bool:
        """
        Returns True if the set is empty.

        :Complexity: O(1)
        """

        return self.elems == 0

    def is_full(self) -> bool:
        """
        Returns True if the set is full, which will never occur because
        arbitrary sized integers will never have a max value.

        :Complexity: O(1)
        """

        return False

    def __contains__(self, item: int) -> bool:
        """
        Returns True if the set contains item, by moving the target bit to the
        rightmost position, and then checking if it is 1.

        :Complexity: O(1)
        """

        return (self.elems >> (item - 1)) & 1

    def add(self, item: T) -> None:
        """
        Adds an item to the set, by moving a 1 bit into the correct position
        in elems.

        :Complexity: O(1)
        """

        self.elems |= 1 << (item - 1)

    def remove(self, item: T) -> None:
        """
        Removes an item to the set, by setting a 0 bit at the position of item
        in elems.

        :Complexity: O(1)
        """

        self.elems &= ~(1 << (item - 1))

    def union(self, other: Set[T]) -> Set[T]:
        """
        Computes the union of two sets.

        :Complexity: O(1), where n and m are the sizes
        of self and other respectively.
        """

        res = BVSet()

        res.elems = self.elems | other.elems

        return res

    def intersection(self, other: Set[T]) -> Set[T]:
        """
        Computes the intersection of two sets.

        :Complexity: O(1),
        where n and m are the sizes of self and other respectively.
        """

        res = BVSet()

        res.elems = self.elems & other.elems

        return res

    def difference(self, other: Set[T]) -> Set[T]:
        """
        Computes the difference of two sets.

        :Complexity: O(1), where n and m are the sizes
        of self and other respectively.
        """

        res = BVSet()

        res.elems = self.elems & ~(other.elems)

        return res
