# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root,-math.inf)]
        ans = 0

        while stack:
            node,maxVal = stack.pop()
            if node.val >= maxVal:
                ans+=1
            if node.left:
                stack.append((node.left,max(node.val,maxVal)))
            if node.right:
                stack.append((node.right,max(node.val,maxVal)))
        return ans




        # def dfs(node,maxVal):
        #     if not node:
        #         return 0
        #     ans = 1 if node.val>=maxVal else 0
        #     maxVal = max(maxVal,node.val)
        #     ans += dfs(node.left,maxVal)
        #     ans+= dfs(node.right,maxVal)
        #     return ans
        # return dfs(root,root.val)
        