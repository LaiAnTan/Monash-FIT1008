from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class PriorityQueue(ABC, Generic[T]):
    
    def __init__(self) -> None:
        self.length = 0
    
    @abstractmethod
    def get_max(self) -> T:
        pass
    
    @abstractmethod
    def add(self, item: T) -> None:
        pass
    
    def __len__(self) -> int:
        return self.length