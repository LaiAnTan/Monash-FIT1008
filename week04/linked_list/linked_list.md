# Linked List

A variation of the List ADT that uses **nodes** that link to one another.

Each node contains a pointer to the next node and also the item that is stored in it.

Links are formed when each node points to the next one.

For example:

```python
(1) -> (2) -> (3) -> (4)
```

## Advantages

- fast deletion and insertion of item
- easily resizible
- less space used than array based list if the array is relatively empty

## Disadvantages

- more space used than array based list if the array is relatively full
- random access is slow

## Operations

The operations of a linked list are pretty much similar to that of a list.

However, the implementation and time complexities of the operations will be different.

## Implementation

[Linked list implementation](linked_list.py).
