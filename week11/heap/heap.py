from __future__ import annotations

# for path to import assets
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from typing import TypeVar, Generic
from assets.ref_array import ArrayR

T = TypeVar('T')

class Heap(Generic[T]):
    
    def __init__(self) -> None:
        
        self.array = ArrayR()
        self.length = 0