# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [0]

        def dfs(root):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            mid = False
            if root == p or root == q:
                mid = True
            if mid + left + right >= 2:
                ans[0] = root
            return mid or left or right
        dfs(root)
        return ans[0]


        