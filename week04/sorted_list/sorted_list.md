# Sorted List

An abstract data type that stores items somewhat like an array (i.e. dynamic array), sorting the items as they are inserted.

Item access, insertion and deletion is allowed anywhere.

For example, let x be a sorted list:

```python
x = [1, 2, 4, 5]

x.add(3)

x => [1, 2, 3, 4, 5]
```

## Operations

The operations of a sorted list are pretty much similar to that of a list.

However, operations like index will use a different approach as the list is already sorted.

The add operation will also have to handle inserting the item at its correct place.

## Implementations

First, we implement the [abstract base class for a generic sorted list ADT](generic_sorted_list.py).

We can use [fixed-sized arrays](array_sorted_list.py) to implement a list.
