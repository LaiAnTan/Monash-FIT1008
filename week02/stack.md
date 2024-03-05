# Stack

An abstract data type that stores items in a
**Last In First Out** process.

Item access is only allowed at the top of the stack.

For example:

```python
| 1 | <- top of the stack
| 3 |
| 4 |
| 2 |
| 5 | <- bottom of the stack
-----
```

## Main operations

- push: add an item to the top of the stack
- pop: remove an item from the top of the stack

## Other operations

- peek: look at item at the top of the stack
- length: size of stack
- full: if the stack is full
- empty: if the stack is empty
- clear: clear all items from the stack

## Implementation

We can use [fixed-sized arrays to implement stacks](stack.py).

## Common use cases

- Reversing a sequence

1. Create a stack with a max capacity the length of the sequence
2. Traverse the sequence, pushing each item onto the stack
3. Initialise the return container.
4. Pop each elemnt from the stack and insert it into the container.
