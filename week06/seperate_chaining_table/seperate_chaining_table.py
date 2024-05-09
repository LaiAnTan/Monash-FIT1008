from __future__ import annotations
from typing import Generic

# for path to import assets
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from hash_table.generic_hash_table import HashTable, K, V
from assets.ref_array import ArrayR


class Node(Generic[K, V]):

    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return f"({self.key}, {self.value}){' -> ' if self.next else ''}"

class SeperateChainingTable(HashTable[str, V]):
    
    """
    Simple Hash Table implementation with Seperate Chaining as
    collision resolution method.
    
    Keys must be string for simplicity sake.
    """
    
    TABLE_SIZE = 31
    
    def __init__(self) -> None:
        """
        Initialise the Hash Table.
        """
        
        self.count = 0
        self.array: ArrayR[Node] = ArrayR(self.TABLE_SIZE)

    def hash(self, key: str) -> int:
        
        BASE = 31415
        ALT = 27183
        value = 0
        for char in key:
            value = (value * BASE + ord(char)) % self.TABLE_SIZE
            BASE = BASE * ALT % (self.TABLE_SIZE - 1)
        return value

    def __len__(self) -> int:
        """
        Returns the number of elements in the hash table.
        """
        return self.count
    
    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True
    
    def __delitem__(self, key: K) -> None:
        
        position = self.hash(key)
        
        if self.array[position] is None:
            raise KeyError("Key not found")
        
        if self.array[position].key == key:
            self.array[position] = self.array[position].next
        else:
            
            prev: Node = self.array[position]
        
            while prev.next:
                
                if prev.next.key == key:
                    prev.next = prev.next.next
                    break
                
                prev = prev.next
            else:
                raise KeyError("Key not found")

        self.count -= 1
    
    def __setitem__(self, key: K, data: V) -> None:
        
        position = self.hash(key)
        
        if self.array[position] is None:
            
            self.array[position] = Node(key, data)
        
        else:
            
            curr: Node = self.array[position]
        
            while curr.next:
                curr = curr.next
            
            curr.next = Node(key, data)
        
        self.count += 1


    def __getitem__(self, key: K) -> V:
        """
        Get the value at a certain key

        :raises KeyError: when the key doesn't exist.
        """
        position = self.hash(key)
        
        if self.array[position] is None:
            raise KeyError("Key not found")
        
        curr: Node = self.array[position]
        
        while curr.next:
            
            if curr.key == key:
                return curr.value
            
            curr = curr.next
                
        raise KeyError("Key not found")
        
    
    def keys(self) -> list[K]:
        
        keys = []
        
        for item in self.array:
            
            curr: Node = item
            
            while curr:
                keys.append(curr.key)
                curr = curr.next

        return keys

    def values(self) -> list[V]:
        
        values = []
        
        for item in self.array:
            
            curr: Node = item
            
            while curr:
                values.append(curr.value)
                curr = curr.next

        return values

    def is_empty(self) -> bool:
        return self.count == 0
    
    def __str__(self) -> str:
        
        rs = ""
        
        for pos, item in enumerate(self.array):
            
            s = ""
            curr: Node = item
            
            while curr:
                s += str(curr)
                curr = curr.next
            
            rs += f"{pos}: {s}\n"
        
        return rs

if __name__ == "__main__":
    
    sct = SeperateChainingTable()
    
    sct["lin"] = 1
    sct["leg"] = 2
    sct["mine"] = 3
    sct["linked"] = 4
    sct["limp"] = 5
    sct["mining"] = 6
    sct["jake"] = 7
    sct["linger"] = 8

    print(sct)
    print(sct.keys())
    print(sct.values())
    
    del sct["mine"]
    del sct["linger"]
    del sct["lin"]
    del sct["leg"]
    del sct["jake"]
    del sct["mining"]
    del sct["limp"]
    del sct["linked"]
    
    print(sct)