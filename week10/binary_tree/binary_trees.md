# Binary Trees

A tree where each node can have at most **2** children.

## Balance of Tree

### Height Balanced Binary Tree

A binary tree is balanced in terms of its height when **the difference between the height of the left subtree and that of the right subtree is at most 1**.

![balanced_btree](/assets/balanced_btree.png)

### Other types of balanced trees

- weight balanced: number of nodes of the subtree

## Perfect Binary Trees

Criteria for perfect binary trees:

- all parents have two children
- all leaf nodes are at the same level

For a perfect binary tree with height $k$, the number of nodes in said perfect binary tree, $N = 2^{k+1}-1$.

### Height of Perfect binary tree

Since the number of nodes in a perfect binary tree, $N = 2^{k+1}-1$,

$$N = 2^{k+1}-1$$
$$N + 1= 2^{k+1}$$
$$log_{2}(N + 1)= k+1$$
$$log_{2}(N + 1) - 1= k$$

The height of a balanced tree in terms of the number of nodes is $O(log(N))$.

## Binary Tree Traversal

There are a few common methods of binary tree traversal, which are:

- preorder
- inorder
- postorder

All of these methods traverse the **left subtree** before the **right subtree**.

The name of the traversal method depends on when the root node is processed.

### Preorder Traversal

root -> left subtree -> right subtree

![preorder](/assets/preorder.png)

### Inorder Traversal

left subtree -> root -> right subtree

![inorder](/assets/inorder.png)

### Postorder Traversal

left subtree -> right subtree -> root

![inorder](/assets/postorder.png)

## Expression Trees

A variant of binary trees, built using operands and operators.

Operands are situated at the leaf nodes, while operators are situated at the inner nodes.

a.k.a. Parse Trees

Used in compilers to represent expressions.

### Expression Tree Traversal and Expression Notation

- Preorder Traversal -> Prefix Notation

- Inorder Traversal -> Infix Notation

- Postorder Traversal -> Postfix Notation (Reverse Polish Notation)
