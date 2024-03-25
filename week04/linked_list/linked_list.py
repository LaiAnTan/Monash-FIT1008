from __future__ import annotations
from typing import Generic
from week03.list.generic_list import List, T
from week05.linked_list_iterator.linked_list_iterator import LinkedListIterator

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))


class Node(Generic[T]):

    def __init__(self, item: T = None) -> None:
        self.item = item
        self.next = None


class LinkedList(List[T]):

    def __init__(self) -> None:
        """
        Initialises a Linked List.

        :Complexity: O(1)
        """
        super().__init__()
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at position index.

        :Complexity: O(n)
        """
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        """
        Gets the item at position index.

        :Complexity: O(n)
        """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item

    def append(self, item: T) -> None:
        new = Node(item)
        end = self.__get_node_at_index(len(self) - 1)
        end.next = new

    def insert(self, index: int, item: T) -> None:
        """
        Insert an item at the specified index

        :Complexity: O(n) where n is the length of the list
        """
        new_node = Node(item)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.__get_node_at_index(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self.length += 1

    def delete(self, index) -> T:
        """
        Delete an item at the specified index

        :raise ValueError: if list is empty or index out of bounds
        :Complexity: O(n) where n is the length of the list
        """

        if self.is_empty():
            raise ValueError("List is empty")

        if index == 0:
            self.head = self.head.next
        elif index > 0:

            prev = self.__get_node_at_index(index - 1)
            item = prev.next.item
            prev.next = prev.next.next

        else:
            raise ValueError("Index out of bounds")

        self.length -= 1
        return item

    def index(self, item: T) -> int:
        """
        Look for an item's index in the linked list.

        :raise ValueError: if the item is not found
        :Complexity: O(n * comp) where n is the size of the list
        """
        curr = self.head

        for i in range(len(self)):
            if curr.item == item:
                return i
            curr = curr.next

        raise ValueError("Item not in list")

    def remove(self, item: T) -> None:
        """
        Removes the first occurence of an item.

        :Complexity: O(delete)
        """

        index = self.index(item)
        self.delete(index)

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
        Clears the stack.

        :Complexity: O(1)
        """

        self.length = 0

    def __get_node_at_index(self, index: int) -> Node:
        """
        Gets the node at position index in the linked list.

        :Complexity: O(n) where n is the length of the linked list
        """

        if index < 0 or index >= len(self):
            raise ValueError("Index out of bounds")

        curr: Node = self.head

        for _ in range(index):
            curr = curr.next

        return curr

    # --- Week 05 ---

    def __iter__(self) -> LinkedListIterator[T]:
        return LinkedListIterator(self.head)
