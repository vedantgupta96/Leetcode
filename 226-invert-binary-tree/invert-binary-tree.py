# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            stack = [root]
            while stack:
                node = stack.pop()

                node.right,node.left = node.left, node.right

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            # left = root.left
            # right = root.right
            # root.left = right
            # root.right = left
            # self.invertTree(root.left)
            # self.invertTree(root.right)
        return root