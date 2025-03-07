# Binary Search Trees

A binary tree with a few more properties:

- each node has a unique key
- all keys in the **left subtree of a node are less than the key of the node**
- all keys in the **right subtree of a node are greater than the key of the node**

Advantages of BST:

- good for searching and for inserting and deleting
- can be traversed in particular orders

## Time complexity of operations

let N be the number of nodes in the BST.

| Operation       | Unbalanced BST Best Case | Unbalanced BST Worst Case | Balanced BST Best Case | Balanced BST Worst Case |
|-----------------|--------------------------|---------------------------|------------------------|-------------------------|
| Search / Lookup | O(1)                     | O(N)                      | O(1)                   | O(log(N))               |
| Insert          | O(1)                     | O(N)                      | O(log(N))              | O(log(N))               |
| Delete          | O(1)                     | O(N)                      | O(log(N))              | O(log(N))               |

Notes:

Unbalanced BST Best Case insertion is O(1) when you insert an element into the other subtree with no nodes from the root.

## Tree sort

Sorting using a BST.

1. Insert all elements from the list into the BST
2. Perform Inorder iteration through the BST to obtain sorted list.

Time complexity:

let N be the number of elements to sort.

Best-case: `O(N log (N))` when the insertion of elements into the BST produces a balanced BST.
Worst-case: `O(N^2)` when the insertion of elements into the BST produces a totally unbalanced BST (degraded into a linked list).
