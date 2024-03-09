# Set

An ADT used to store unique items.

Sets are implementations of mathematical sets, where:

- Elements in a set are unordered
- No duplicates are allowed

Set operations can be performed on these sets, such as:

- Union
- Intersection
- Difference

## Main Operations

- add: add an element to the set
- remove: removes an element from the set
- member: check if an element is in the set
- union: get the union of two sets
- intersection: get the intersection of two sets
- difference: get the difference of two sets

## Other operations

- length: number of items in set
- empty: if the set is empty
- clear: clear all items from the set

## Implementation

First, we implement the [abstract base class for a generic set ADT](generic_set.py).

We can use [fixed-sized arrays](array_set.py) or [bit vectors](bit_vector_set.py) to implement sets.

> Bit Vector implementation of a set is basically just a string of 0s and 1s, with 0 indicating absence and 1 indicating presence of a particular element.

## Fixed-sized Array vs Bit Vector implementation of Set

Fixed-sized Array:

- store items of any type
- obtaining size of a set is cheap: O(1)
- other operations are expensive

Bit Vector:

- store integers only
- number of items is limited by number of bits in bit vectors (arch dependent)
- all operations except for obtaining size of the set is cheap: O(1)
