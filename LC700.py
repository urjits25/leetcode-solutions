'''

SEARCH IN A BINARY SEARCH TREE

Given the root node of a binary search tree (BST) and a value. 
Find the node in the BST that the node's value equal to the given value. 
Return the subtree rooted with that node. If such node doesn't exist, return NULL.

'''

def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    elif root.val < val:
        return self.searchBST(root.right, val)
    return self.searchBST(root.left, val)
