from typing import TypeVar, Generic, Callable

T = TypeVar('T')

class BinaryTreeNode(Generic[T]):
    
    def __init__(self, item: T = None) -> None:
        
        self.item = item
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.item)

class BinaryTree(Generic[T]):
    
    def __init__(self) -> None:
        
        self.root = None
        
    def is_empty(self) -> bool:

        return self.root is None
    
    def preorder(self, f: Callable) -> None:
        
        self.preorder_aux(self.root, f)
        
    def preorder_aux(self, current: BinaryTreeNode[T], f: Callable) -> None:
        """
        Applies a function f onto each node of the binary tree through preorder traversal.
        
        :complexity: O(N * f), where 
            N is the number of nodes in the Binary Tree, and 
            f is the complexity of the function.
        """
        
        if current is None:
            return

        f(current)
        self.preorder_aux(current.left, f)
        self.preorder_aux(current.right, f)
    
    def inorder(self, f: Callable) -> None:
        
        self.inorder_aux(self.root, f)
    
    def inorder_aux(self, current: BinaryTreeNode[T], f: Callable) -> None:
        """
        Applies a function f onto each node of the binary tree through inorder traversal.
        
        :complexity: O(N * f), where 
            N is the number of nodes in the Binary Tree, and 
            f is the complexity of the function.
        """
        
        if current is None:
            return

        self.inorder_aux(current.left, f)
        f(current)
        self.inorder_aux(current.right, f)

    def postorder(self, f: Callable) -> None:
        
        self.postorder_aux(self.root, f)
    
    def postorder_aux(self, current: BinaryTreeNode[T], f: Callable) -> None:
        """
        Applies a function f onto each node of the binary tree through postorder traversal.
        
        :complexity: O(N * f), where 
            N is the number of nodes in the Binary Tree, and 
            f is the complexity of the function.
        """
        
        if current is None:
            return

        self.postorder_aux(current.left, f)
        self.postorder_aux(current.right, f)
        f(current)

if __name__ == "__main__":

    btree: BinaryTree = BinaryTree()

    btree.root = BinaryTreeNode(43)
    btree.root.left = BinaryTreeNode(31)
    btree.root.right = BinaryTreeNode(64)
    btree.root.left.left = BinaryTreeNode(20)
    btree.root.left.left.right = BinaryTreeNode(28)
    btree.root.left.right = BinaryTreeNode(40)
    btree.root.left.right.left = BinaryTreeNode(33)
    btree.root.right.left = BinaryTreeNode(56)
    btree.root.right.left.left = BinaryTreeNode(47)
    btree.root.right.left.right = BinaryTreeNode(59)
    btree.root.right.right = BinaryTreeNode(89)
    
    preorder = []
    inorder = []
    postorder = []
    
    btree.preorder(lambda x: preorder.append(x.item))
    btree.inorder(lambda x: inorder.append(x.item))
    btree.postorder(lambda x: postorder.append(x.item))
    print(f"Preorder: {preorder}")
    print(f"Inorder: {inorder}")
    print(f"Postorder: {postorder}")