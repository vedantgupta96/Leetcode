# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = [0]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            dia = left+right
            ans[0] = max(ans[0], dia)
            return 1 + max(left,right)
        dfs(root)
        return ans[0]
        