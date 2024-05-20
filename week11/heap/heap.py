from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from typing import TypeVar, Generic
from assets.ref_array import ArrayR
from random import randint

T = TypeVar('T')

class Heap(Generic[T]):
    
    MIN_CAPACITY = 1
    
    def __init__(self, max_size: int) -> None:
        
        self.array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)
        self.length = 0
    
    def __len__(self) -> int:
        return self.length
    
    def is_full(self) -> bool:
        return self.length + 1 == len(self.array)

    def add(self, element: T) -> bool:
        """
        Add an element to the heap.
        
        :complexity: O(log (N))
        """
        
        has_space_left = not self.is_full()
        
        if has_space_left:
            self.length += 1
            self.array[self.length] = element
            self.rise(self.length)
        
        return has_space_left
        
        
    def rise(self, index: int) -> None:
        """
        Rise element at index to its correct position.
        
        We swap the node with its parent until it is smaller than its parent.
        
        :complexity: O(log (N))
        """
        
        while index > 1 and self.array[index] > self.array[index // 2]:
            self.array[index], self.array[index // 2] = self.array[index // 2], self.array[index]
            index = index // 2
    
    def get_max(self) -> T:
        
        if self.length == 0:
            raise ValueError("Heap is empty")
        
        max_elem = self.array[1]
        self.length -= 1

        if self.length > 0:
            self.array[1] = self.array[self.length + 1]
            self.sink(1)
        
        return max_elem
    
    def sink(self, index: int) -> None:
        """
        Sink element at index to its correct position.
        
        We swap the node with its largest child until the end.
        
        :complexity: O(log(N))
        """
        
        while 2 * index <= self.length:
            
            child = self.largest_child(index)
            if self.array[index] >= self.array[child]:
                break
            
            self.array[index], self.array[child] = self.array[child], self.array[index]
            index = child
        
    
    def largest_child(self, index: int) -> int:
        """
        Returns the index of the largest child of node at position index.
        """
        
        if 2 * index == self.length or \
            self.array[2 * index] > self.array[2 * index + 1]:
            return 2 * index
        else:
            return 2 * index + 1
    
    @classmethod
    def heapify(cls, arr: ArrayR[T]) -> Heap[T]:
        """
        Construct a heap from an array.
        
        :complexity: O(N)
        """
        
        self = Heap(2 * len(arr) + 2)
        self.length = len(arr)
            
        for i in range(len(arr)):
            self.array[i + 1] = arr[i]
        
        for i in range(len(arr), 0, -1):
            self.sink(i)

        return self

if __name__ == "__main__":
    
    maxheap = Heap(5)
    
    for i in range(5):
        maxheap.add(i + 1)
    
    print(f"Max heap: {[maxheap.get_max() for _ in range(5)]}")
    
    arr = ArrayR(10)
    for i in range(10):
        arr[i] = randint(1, 50)
    
    heapified = Heap.heapify(arr)
    
    print(f"Max heap: {[heapified.get_max() for _ in range(10)]}")