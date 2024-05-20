from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from assets.ref_array import ArrayR
from week10.binary_search_tree.binary_search_tree import BinarySearchTree, InOrderIterator
from random import randint

def tree_sort(arr: list):
    
    bst = BinarySearchTree()
    
    for elem in arr:
        bst.insert(elem, elem)
    
    for i, elem in enumerate(InOrderIterator(bst)):
        arr[i] = elem

if __name__ == "__main__":
    
    l = []
    while len(l) <= 10:
        
        r = randint(1, 50)
        
        if r not in l:
            l.append(r)
    
    tree_sort(l)
    
    print(f"Sorted: {l}")
    