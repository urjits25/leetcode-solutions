'''

BINARY TREE LEVEL ORDER TRAVERSAL

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
  
    3
   / \          
  9  20      ---->  [[3], [9, 20], [15, 7]]
    /  \
   15   7 

'''

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    ans, level = [], [root]
    while level:
        ans.append([l.val for l in level])                      # ---- Add ListNode vals from previous levels

        new = []
        for n in level:                                         # ---- Add children of current level ListNodes to next level
            if n.left:
                new.append(n.left)
            if n.right:
                new.append(n.right)

        if level is not new:                                    # ---- Exit if we reach leaf nodes
            level = new
        else:
            level = []

    return ans
