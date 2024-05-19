from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from typing import TypeVar, Generic, List

K = TypeVar('K')
I = TypeVar('I')

from week05.linked_stack.linked_stack import LinkedStack

class BinarySearchTreeNode(Generic[K, I]):
    
    def __init__(self, key: K, item: I = None) -> None:
        
        self.key = key
        self.item = item
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return " (" + str(self.key) + ", " + str(self.item) + ")"
    
    def __repr__(self) -> str:
        return "(" + str(self.key) + ", " + str(self.item) + ")"

class BinarySearchTree(Generic[K, I]):
    
    def __init__(self) -> None:
        
        self.root = None
        self.length = 0
    
    def is_empty(self) -> bool:
        
        return self.root is None

    def __contains__(self, key: K) -> bool:
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True
    
    def __getitem__(self, key: K) -> I:
        return self.getitem_aux(self.root, key)
        
    def getitem_aux(self, current: BinarySearchTreeNode[K, I], key: K) -> I:
        """
        :complexity best: O(log N) when the tree is balanced, where
            N is the number of nodes in the tree.
        :complexity worst: O(N) when the tree is unbalanced, where
            N is the number of nodes in the tree.
        """
        
        if current is None:
            raise KeyError("Key not found")
        elif current.key == key:
            return current.item
        
        if key < current.key:
            self.getitem_aux(current.left, key)
        elif key > current.key:
            self.getitem_aux(current.right, key)

    def insert(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BinarySearchTreeNode[K, I], key: K, item: I) -> I:
        """
        :complexity best: O(log N) when the tree is balanced, where
            N is the number of nodes in the tree.
        :complexity worst: O(N) when the tree is unbalanced, where
            N is the number of nodes in the tree.
        """
        
        if current is None:
            current = BinarySearchTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:
            raise ValueError("Item already exists")

        return current

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.setitem_aux(key, item)

    def setitem_aux(self, current: BinarySearchTreeNode[K, I], key: K, item: I) -> BinarySearchTreeNode[K, I]:
        """
        :complexity best: O(log N) when the tree is balanced, where
            N is the number of nodes in the tree.
        :complexity worst: O(N) when the tree is unbalanced, where
            N is the number of nodes in the tree.
        """
        
        
        if current.link is None:
            current = BinarySearchTreeNode(key, item)
        elif key < current.key:
            current.left = self.setitem_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.setitem_aux(current.right, key, item)
        else:
            current.item = item

        return current

    def __delitem__(self, key: K) -> None:
        self.delitem_aux(self.root, key)
    
    def delitem_aux(self, current: BinarySearchTreeNode[K, I], key: K) -> BinarySearchTreeNode[K, I]:
        """
        :complexity best: O(log N) when the tree is balanced, where
            N is the number of nodes in the tree.
        :complexity worst: O(N) when the tree is unbalanced, where
            N is the number of nodes in the tree.
        """
        
        if current is None:
            raise ValueError("Key not found")
        
        if key < current.key:
            current.left = self.delitem_aux(current.left, key)
        elif key > current.key:
            current.right = self.delitem_aux(current.right, key)
        else:
            if self.is_leaf(current):
                self.length -= 1
                return None

            elif current.left is None:
                self.length -= 1
                return current.right
                
            elif current.right is None:
                self.length -= 1
                return current.left

            # both child found
            # successor to replace the deleted node
            successor = self.get_successor(current)
            current.key = successor.key
            current.item = successor.item
            
            # delete successor
            current.right = self.delitem_aux(current.right, successor.key)
        
        return current
    
    def get_successor(self, current: BinarySearchTreeNode[K, I]) -> BinarySearchTreeNode[K, I]:
        """
        Function that locates the successor of a node in a subtree, where current is
        the root of the subtree.
        """
        if current is None:
            return None
        return self.get_minimum(current.right)
    
    def get_minimum(self, current: BinarySearchTreeNode[K, I]) -> BinarySearchTreeNode[K, I]:
        
        if current is None:
            return None
        if current.left is None:
            return current
        return self.get_minimum(current.left)
    
    def is_leaf(self, node: BinarySearchTreeNode[K, I]) -> bool:
        return node.left is None and node.right is None

    def get_leaves(self) -> List[BinarySearchTreeNode[K, I]]:
        result = []
        self.get_leaves_aux(self.root, result)
        return result
    
    def get_leaves_aux(self, current: BinarySearchTreeNode[K, I], result: List[BinarySearchTreeNode[K, I]]):
        
        if current is not None:
            if self.is_leaf(current):
                result.append(current)
            else:
                self.get_leaves_aux(current.left, result)
                self.get_leaves_aux(current.right, result)
    
    def __iter__(self):
        return InOrderIterator(self)

class PreOrderIterator():
    
    def __init__(self, bst: BinarySearchTree[K, I]) -> None:
        self.stack = LinkedStack()
        self.stack.push(bst.root)
    
    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> None:
        
        if self.stack.is_empty():
            raise StopIteration
        
        current = self.stack.pop()
        
        if current.right is not None:
            self.stack.push(current.right)
        if current.left is not None:
            self.stack.push(current.left)
        
        return current.item

class InOrderIterator():
    
    def __init__(self, bst: BinarySearchTree[K, I]) -> None:
        self.stack = LinkedStack()
        self.current = bst.root
    
    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> None:
        
        # handle all left
        while self.current:
            self.stack.push(self.current)
            self.current = self.current.left
        
        if self.stack.is_empty():
            raise StopIteration
        
        result = self.stack.pop()
        
        # then right
        self.current = result.right
        
        return result.item

class PostOrderIterator():
    
    def __init__(self, bst: BinarySearchTree[K, I]) -> None:
        self.hold = LinkedStack() # holding zone
        self.reverse = LinkedStack() # stack to reverse order
        self.hold.push(bst.root)
    
    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> None:
        
        while len(self.hold) > 0:
            current = self.hold.pop()
            self.reverse.push(current)
        
            if current.left is not None:
                self.hold.push(current.left)
            if current.right is not None:
                self.hold.push(current.right)
        
        if len(self.reverse) == 0:
            raise StopIteration
        else:
            return self.reverse.pop().item

if __name__ == "__main__":
    
    bst: BinarySearchTree = BinarySearchTree()
    
    l = [43, 31, 64, 20, 28, 40, 56, 47, 59, 89]
    
    for num in l:
        bst.insert(num, num)
    
    print(f"In Order: {[x for x in bst]}")
    print(f"Pre Order: {[x for x in PreOrderIterator(bst)]}")
    print(f"Post Order: {[x for x in PostOrderIterator(bst)]}")
    print(f"All leaves: {bst.get_leaves()}")
    
    for num in reversed(l):
        del bst[num]

    