from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from typing import Callable

from generic_priority_queue import PriorityQueue, T
from week03.list.array_list import ArrayList
from week04.sorted_list.array_sorted_list import ArraySortedList

class UnsortedArrayListPriorityQueue(PriorityQueue[T]):
    
    def __init__(self, key: Callable = lambda x: x) -> None:
        super().__init__()
        self.list = ArrayList(1)
        self.key = key
    
    def get_max(self) -> T:
        """
        :complexity: O(N), where 
            N is the number of elements in the Priority Queue.
        """
        if len(self) == 0:
            raise ValueError("Priority Queue is empty")
        
        # brain dead ArrayList implementation made me do this
        item = max(self.list[0:self.list.length], key=self.key)
        
        self.list.remove(item)
        
        return item
    
    def add(self, item: T) -> None:
        """
        :complexity: O(1)
        """
        self.list.append(item)
    
    def __len__(self) -> int:
        return len(self.list)
    
    def __str__(self) -> str:
        return str(self.list)

class SortedArrayListPriorityQueue(PriorityQueue[T]):

    def __init__(self, key: Callable = lambda x: x) -> None:
        super().__init__()
        self.list = ArraySortedList(2)
        self.key = key

    def get_max(self) -> T:
        """
        :complexity: O(1)
        """
        
        if len(self) == 0:
            raise ValueError("Priority Queue is empty")
        
        # remove from back is O(1)
        return self.list.delete(len(self.list) - 1)
    
    def add(self, item: T) -> None:
        """
        :complexity: O(N), where 
            N is the number of elements in the Priority Queue.
        """
        self.list.add(item)
    
    def __len__(self) -> int:
        return len(self.list)
    
    def __str__(self) -> str:
        return str(self.list)

if __name__ == "__main__":
    
    l = [2, 3, 5, 1, 4]
    
    maxpq_sorted = SortedArrayListPriorityQueue()
    max_pq_unsorted = UnsortedArrayListPriorityQueue()
    
    for e in l:
        maxpq_sorted.add(e)
        max_pq_unsorted.add(e)
    
    print(f"maxpq (unsorted): {max_pq_unsorted}")
    print(f"maxpq (sorted): {maxpq_sorted}")

    print(f"maxpq (unsorted): {[max_pq_unsorted.get_max() for _ in range(5)]}")
    print(f"maxpq (sorted): {[maxpq_sorted.get_max() for _ in range(5)]}")