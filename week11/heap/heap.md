# Heap

A variant of a binary tree, which has two special properties:

- complete:

  - Every level of the binary tree except the last one is full
  - The last level is filled from the left

- heap-ordered: Each child is smaller than (or equal to) its parent

## Types of heaps

- min heap: minimum at the root of the binary tree
- max heap: maximum at the root of the binary tree

## Implementations

- Binary Tree (complex, extra memory needed)
- Array

## Heap sort

In place sort using heaps.

1. Build a heap using heapify O(N)
2. get_max() from the heap N times O(N log(N))

Time complexity: `O(N log (N))`, Space complexity: O(1)
