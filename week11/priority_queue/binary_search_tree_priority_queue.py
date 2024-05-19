from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from week10.binary_search_tree.binary_search_tree import BinarySearchTreeNode, BinarySearchTree, K, I

from generic_priority_queue import PriorityQueue, T

class BinarySearchTreePriorityQueue(PriorityQueue[T]):
    
    def __init__(self) -> None:
        super().__init__()
        self.bst = BinarySearchTree()
    
    def get_max(self) -> T:
        
        item = self.get_max_aux(self.bst.root)

        del self.bst[item.key]
        
        return item.item
    
    def get_max_aux(self, current: BinarySearchTreeNode[K, I]):
        
        if current is None:
            return None
        if current.right is None:
            return current
        return self.get_max_aux(current.right)

    def add(self, item: T) -> None:
        
        self.bst.insert(item, item)
        
    def __len__(self) -> int:
        return len(self.bst)

if __name__ == "__main__":
    
    l = [2, 3, 5, 1, 4]
    
    pq = BinarySearchTreePriorityQueue()
    
    for e in l:
        pq.add(e)

    print(f"pq: {[pq.get_max() for _ in range(5)]}")