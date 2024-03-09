# Queue

An abstract data type that stores items in a **First In First Out** process.

Item access is only allowed at the front of the queue.

For example:

```python
                      ---------
Front of the queue <- 1 3 4 2 5 <- Back of the queue
                      ---------
```

## Main operations

- append: add an item to the back of the queue
- serve: take an item off the front of the queue

## Other operations

- length: number of items in queue
- full: if the stack is full
- empty: if the stack is empty
- clear: clear all items from the stack

## Implementations

First, we implement the [abstract base class for a generic queue ADT](generic_queue.py).

We can use fixed-sized arrays to implement queues.

A [linear queue](linear_queue.py) is the naive implementation of a queue using fixed-sized arrays.

A [circular queue](circular_queue.py) is an improvement to the linear queue.

### Downfalls of the linear queue



## Common use cases

Scheduling andbuffering

- async / await