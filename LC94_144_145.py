'''

BINARY TREE TRAVERSALS - INORDER, PREORDER, POSTORDER

Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
'''

'''
-------------------------------------------------- INORDER --------------------------------------------------
'''
def inorderTraversal(self, root: TreeNode) -> List[int]:        
        
        if not root:
            return []

         # Recursive solution         
         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
        # Iterative Solution, better solution: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/30044
        if not root:
            return []
        
        visited = set()
        ans, stack = [], [root]
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
            else:
                n = stack.pop()
                visited.add(n)
                ans.append(n.val)

                if n.right:
                    stack.append(n.right)                
        return ans

'''
-------------------------------------------------- POSTORDER --------------------------------------------------
'''
def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # Recursive Solution
        return self.postorderTraversal(root.left) +  self.postorderTraversal(root.right) + [root.val]

        # Iterative solution
        ans, stack = [], [root]
        
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            
        return ans[::-1]

'''
-------------------------------------------------- PREORDER --------------------------------------------------
'''
def preorderTraversal(root: TreeNode) -> List[int]:

        if not root:                                                    # ---- Iterative Solution
            return []
        
        ans, stack = [], [root]
        while stack:
            n = stack.pop()
            ans.append(n.val)
            
            children = [n.right, n.left]
            stack.extend([c for c in children if c])
            
        return ans
            
            
        if not root:                                                    # ---- Recursive Solution
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
