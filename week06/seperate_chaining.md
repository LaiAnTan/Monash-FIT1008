# Seperate Chaining

Seperate chaining is a way to address collisions in a hash table.

Simply put, it appends colliding keys to a linked list or balanced tree which contains all the colliding keys for that hash value.

However, this will make the time complexity of operations become O(n).
