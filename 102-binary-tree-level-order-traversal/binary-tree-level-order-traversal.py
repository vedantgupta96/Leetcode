# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans= []
        q = collections.deque()
        q.append(root) #initially queue will always have the root since it's the first level

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:    # making sure we don't add null values, edge case
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(level)
        return ans
            
                
        