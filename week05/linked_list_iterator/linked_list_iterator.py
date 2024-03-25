from __future__ import annotations
from typing import Generic
from week04.linked_list.linked_list import LinkedList, T

# for path to import assets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))


class LinkedListIterator(Generic[T]):

    def __init__(self, list: LinkedList[T]) -> None:
        self.list = list
        self.curr = self.list.head
        self.prev = None

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.curr is not None:
            item = self.curr.item
            self.prev = self.curr
            self.curr = self.curr.next
            return item

        raise StopIteration

    def has_next(self):
        return self.curr is not None

    def peek(self):
        try:
            return self.curr.item
        except AttributeError:
            raise StopIteration("No more elements in list")

    def delete(self) -> T:

        if not self.has_next():
            raise StopIteration("No more elements in list")

        item = self.curr.item
        self.curr = self.curr.next

        if self.prev is None:
            self.list.head = self.curr
        else:
            self.prev.next = self.curr

        self.list.length -= 1

        return item
