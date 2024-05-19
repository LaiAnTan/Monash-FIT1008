# Iterators

Iterators in python refer to objects that can be iterated on (i.e. traverse through all values).

We can implement an iterator class using magic methods like:

- `__iter__`: returns an iterator object of the class
- `__next__`: returns the next item in the sequence

In the main class, we can then define `__iter__` that returns the iterator class.

This allows us to traverse linked lists and the like without accessing the internals (i.e. self.next)

An object that can be iterated on is called an iterable.

The `StopIteration` exception should be raised when there are no more elements to iterate through in the collection.

When we try to iterate using an iterator that has already had its collection of values exhausted and already has raised `StopIteration`, `StopIteration` will be raised indefinitely for every call of `next()` on the iterator.
