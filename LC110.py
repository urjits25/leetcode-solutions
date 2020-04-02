'''

BALANCED BINARY TREE

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

'''

def height(self, node: TreeNode) -> int:                                        # ---- Max height for the given node
    if not node:
        return 0    
    return 1 + max(self.height(node.left), self.height(node.right))

def isBalanced(self, root: TreeNode) -> bool:                                   # ---- Recursive definition
    if not root:
        return True

    return self.isBalanced(root.left) and self.isBalanced(root.right) and \     # ---- Check balance & height diff of each child node
            abs(self.height(root.left) - self.height(root.right)) <= 1
