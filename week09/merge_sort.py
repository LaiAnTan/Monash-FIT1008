from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from assets.ref_array import ArrayR

class Laian:
    
    # version of merge sort that is not in place

    def merge(self, left: list, right: list) -> list:
        
        merged = []
        
        left_idx = 0
        right_idx = 0
        
        while left_idx != len(left) and right_idx != len(right):
            
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        
        for i in range(left_idx, len(left)):
            merged.append(left[i])
            
        for j in range(right_idx, len(right)):
            merged.append(right[j])

        return merged

    def merge_sort(self, arr: list) -> list:
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        
        left = arr[0:mid]
        right = arr[mid:len(arr)]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self.merge(left, right)


class FIT1008:
    
    def merge(self, arr: ArrayR, start: int, mid: int, end: int,
              temp: ArrayR) -> None:
        
        a_idx = start
        b_idx = mid + 1
        for k in range(start, end + 1):
            
            # if first half all used up, copy all of second half over
            if a_idx > mid:
                temp[k] = arr[b_idx]
                b_idx += 1
            
            # if second half all used up, copy all of first half over
            elif b_idx > end:
                temp[k] = arr[a_idx]
                a_idx += 1
            
            # normal sorting
            elif arr[a_idx] <= arr[b_idx]:
                temp[k] = arr[a_idx]
                a_idx += 1
            else:
                temp[k] = arr[b_idx]
                b_idx += 1

    def merge_sort_aux(self, arr: ArrayR, start: int, end: int,
                       temp: ArrayR) -> None:
        
        # same thing as mine but here we use a temp array to store everything
        # and pointers to seperate between them
        
        if not start == end:
            
            mid = (start + end) // 2
            
            self.merge_sort_aux(arr, start, mid, temp)
            self.merge_sort_aux(arr, mid + 1, end, temp)

            self.merge(arr, start, mid, end, temp)
            
            for i in range(start, end + 1):
                arr[i] = temp[i]
    
    def merge_sort(self, arr: list) -> list:

        return self.merge_sort_aux(arr, 0, len(arr) - 1, ArrayR(len(arr)))

if __name__ == "__main__":
    
    l = [5, 4, 3, 2, 1]
    g = [5, 4, 3, 2, 1]
    
    l = Laian().merge_sort(l)
    
    print(l)
    
    FIT1008().merge_sort(g)
    
    print(g)