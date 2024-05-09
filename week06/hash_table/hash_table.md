# Hash Table

An ADT that provides efficient adding, searching and deletion operations.

Each item stored in a hash table must have a unique key.

## Operations

- add
- search
- delete

With a perfect hash table implementation, these operations are expected to run in constant time, i.e. O(1). However, they can still reach O(n) if the hash table is not constructed well.

## Use Cases

- tracking the number of each item
- data caching

## Collision Resolution

There are two main ways to resolve [collisions](hash_function.md/#collision) in a hash table.

- Seperate Chaining: By appending elements that collide to a linked list (or balanced tree)
- Open addressing: By inserting elements that collide into another empty space in the hash table.

## Load Factor

The load factor of a hash table is the ratio of the number of elements in the hash table to the table size.

$$Load\;Factor = \frac{|elements|}{table\;size}$$

It represents the "fullness" of a hash table.
