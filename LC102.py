'''

BINARY TREE LEVEL ORDER TRAVERSAL

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
  
    3
   / \          
  9  20      ---->  [[3], [9, 20], [15, 7]]
    /  \
   15   7 

'''

from collections import deque

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    ans, level = [], [root]

    while level:
    
        ans.append([node.val for node in level if node])
 
        temp = []
        for node in level:
            if node:
                temp.extend([node.left, node.right])
        
        level = [leaf for leaf in temp if leaf]

    return ans
