from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")


class SortedList(ABC, Generic[T]):

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def delete(self, index: int) -> T:
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        pass

    def remove(self, item: T) -> None:
        index = self.index(item)
        self.delete_at_index(index)

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        self.length = 0

    @abstractmethod
    def add(self, item: T) -> None:
        pass
