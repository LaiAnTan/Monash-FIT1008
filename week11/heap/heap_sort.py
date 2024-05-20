from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from assets.ref_array import ArrayR
from week11.heap.heap import Heap
from random import randint

def heap_sort(arr: ArrayR):
    """
    
    :complexity: O(N log(N))
    """
    
    # O(N)
    heap = Heap.heapify(arr)
    
    # O(N log N)
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = heap.get_max()

if __name__ == "__main__":
    
    arr = ArrayR(10)
    for i in range(10):
        arr[i] = randint(1, 50)
    
    heap_sort(arr)
    
    print(f"Sorted: {arr}")
    