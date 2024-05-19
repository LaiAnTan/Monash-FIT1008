# Priority Queue

A queue where each element has a numeric priority.

Elements are processed in descending order of priority, starting from the element with the highest priority.

> FIFO queue can be described as a priority queue where the priority is the time spent inside the queue.

## Main Operations

- add(element): Add an element into the priority queue
- get_max: Serves the element with the highest priority

## Use Cases

- hospital emergency rooms
- job scheduling
- discrete event simulation
- graph algorithms
- genetic algorithms

## Possible implementations

- array
- linked list
- binary search tree
- heap

## Time Complexities

| Implementation     | Sorted | get_max                                   | add                                       |
|--------------------|--------|-------------------------------------------|-------------------------------------------|
| Array              | Yes    | O(1)                                      | O(N)                                      |
| Array              | No     | O(N)                                      | O(1)                                      |
| Linked List        | Yes    | O(1)                                      | O(N)                                      |
| Linked List        | No     | O(N)                                      | O(1)                                      |
| Binary Search Tree | N/A    | O(N) if unbalanced, O(log(N)) if balanced | O(N) if unbalanced, O(log(N)) if balanced |
| Heap               | N/A    | Best O(1), Worst O(log (N))               | Best O(1), Worst O(log (N))               |
