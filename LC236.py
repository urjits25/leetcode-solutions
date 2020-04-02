'''

LOWEST COMMON ANCESTOR OF A BINARY TREE ( W/O PARENT field )

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Definition of LCA: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
                   that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''

# Avoiding Multiple Passes, better solution: https://youtu.be/py3R23aAPCA -> O(N) time and O(H) space
def dfs(root: 'TreeNode', p: 'TreeNode') -> List['TreeNode']:        
    if not root:
        return None

    if root == p or root == q:
        return root

    left_search = self.lowestCommonAncestor(root.left, p, q)
    right_search = self.lowestCommonAncestor(root.right, p, q)

    if left_search and right_search:
        return root
    elif left_search:
        return left_search
    elif right_search:
        return right_search



# Brute-force solution that compares paths of both given nodes -> O(N^2) time and O(H) space
def dfs(root: 'TreeNode', p: 'TreeNode') -> List['TreeNode']:
    if not root:
        return []

    if root == p:
        return [p]

    left_path = self.dfs(root.left, p)
    right_path = self.dfs(root.right, p)

    if left_path:
        return [root] + left_path
    elif right_path:
        return [root] + right_path


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    path_p = self.dfs(root, p)
    path_q = self.dfs(root, q)

    print([c.val for c in path_p])
    print([c.val for c in path_q])

    ans = root
    for a in path_q:
        if a in path_p:
            ans = a
    return ans
