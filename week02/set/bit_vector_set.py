from __future__ import annotations

from generic_set import Set, T


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
