'''

SYMMETRIC BINARY TREE

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

'''


def isSymmetric(root: TreeNode) -> bool:
    return self.isMirror(root.left, root.right) if root else True


def isMirror(left:TreeNode, right:TreeNode) -> bool:
    if left and right and left.val == right.val:                        # ---- If both nodes exist and have equal values
        return self.isMirror(left.left, right.right) and \              # ---- Check the lateral nodes (mirror adjacent)
               self.isMirror(left.right, right.left)

    return True if not left and not right else False                    # ---- Return True if both nodes are None, else False
