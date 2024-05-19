# Trees

## Mathematical Definition

A connected graph that does not contain a cycle (acyclic).

## CS Definition

Rooted trees - one node is marked as the root

- edges are directional (parent -> child)
- sibling nodes might have order (left to right)

## Tree Notation

### Node

A **node** is the basic building block of the tree.
A node usually has a parent and a child.

A node that does not have a parent is called a **root node**.

A node that does not have a child is called a **leaf node**.

All other nodes are called **inner nodes**.

### Edges

Edges in a tree connect nodes to one another.

A **parent node** is connected to a **child node** by an edge.

### Path

A **path** is the sequence of edges from one node to another.

The length of a path is the number of edges traversed from one node to another.

### Subtree

A **subtree** is a tree that is part of a larger tree.

Subtrees can vary, ranging from a single node to the whole original tree itself (every tree is a subtree of itself).

### Depth

The depth of a node is the distance (length of path) of said node from the root

The depth / height of a tree is the max length of a path from the root.

Nodes in the same level have the same depth.

> level and depth can be used interchangably.

### Width

The number of nodes in the level with most nodes.
