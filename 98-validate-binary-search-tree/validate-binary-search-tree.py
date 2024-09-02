# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root,-math.inf,math.inf)]

        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            val = root.val
            if val <=low or val >= high:
                return False
            stack.append((root.left,low,val))
            stack.append((root.right,val,high))
        return True            
 # if node:
            #     if node.left:
            #         stack.append(node.left)
            #     if node.right:
            #         stack.append(node.right)
            #         if node.left.val < node.val and node.right.val > node.val:
            #             return True
        