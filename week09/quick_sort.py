from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from assets.ref_array import ArrayR
from abc import ABC, abstractmethod

class QuickSort(ABC):
    
    def quick_sort(self, arr):
        
        self.quick_sort_aux(arr, 0, len(arr) - 1)
    
    
    def quick_sort_aux(self, arr: list, start: int, end: int) -> list:
        
        if start >= end or start < 0:
            return
        
        boundary = self.partition(arr, start, end)
        
        self.quick_sort_aux(arr, start, boundary - 1)
        self.quick_sort_aux(arr, boundary + 1, end)

    
    @abstractmethod
    def partition(self, arr: list, start: int, end: int) -> int:
        pass


class LomutoPartitionQuickSort(QuickSort):
    
    def _swap(self, arr: list, i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]
    
    def partition(self, arr: list, start: int, end: int) -> int:
        
        if start == end:
            return

        mid = (start + end) // 2
        pivot = arr[mid]
        
        print(f"Pivot: {pivot}")
        
        self._swap(arr, start, mid)
        boundary = start
        
        for i in range(start, end + 1):
            
            if arr[i] < pivot:
                boundary += 1
                self._swap(arr, i, boundary)
                
        # move boundary to correct place
        self._swap(arr, start, boundary)
        
        print(f"Array after partition with pivot {pivot}: {arr}")
        
        return boundary


class HoarePartitionQuickSort(QuickSort):
    
    def _swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def partition(self, arr: list, start: int, end: int) -> int:
        
        if start == end:
            return

        mid = (start + end) // 2
        pivot = arr[mid]
        
        print(f"Pivot: {pivot}")
        
        while True:
            
            while arr[start] < pivot:
                start += 1
                
            while arr[end] > pivot:
                end -= 1
        
            if start >= end:
                
                print(f"Array after partition with pivot {pivot}: {arr}")
                
                return end
            
            self._swap(arr, start, end)


if __name__ == "__main__":
    
    l = [5, 4, 3, 2, 1, 6, 8, 10, 9, 7]
    g = [5, 4, 3, 2, 1, 6, 8, 10, 9, 7]
    
    LomutoPartitionQuickSort().quick_sort(l)
    
    print(l)
    
    HoarePartitionQuickSort().quick_sort(g)
    
    print(g)