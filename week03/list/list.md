# List

An abstract data type that stores items somewhat like an array (i.e. dynamic array).

Item access, insertion and deletion is allowed anywhere.

For example:

```python
[1, 2, 3, 4, 5]
```

## Operations

The operations of a list are not well defined, as there are many possible operations that can be performed.

- get: get the element at a certain position
- set: set the element at a certain position
- length: number of items in list
- empty: if the stack is empty
- index: get the index of the first occurence of an element
- append: append an item
- insert: insert an item at a certain position
- remove: remove the first occurence of an item
- clear: clear the list

And many more.

## Implementations

First, we implement the [abstract base class for a generic list ADT](generic_list.py).

We can use [fixed-sized arrays](array_list.py) to implement a list.

We can also use nodes to implement a list, a.k.a [Linked List](../../week04/linked_list/)

There is also a variant of a list that keeps items in a particular order, a.k.a [Sorted List](../../week04/sorted_list/)

## Common use cases
