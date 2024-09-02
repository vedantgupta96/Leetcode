# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                temp.append(node.val)
                q.append(node.right)
                q.append(node.left)
        heapq.heapify(temp)
        while k>1:
            heapq.heappop(temp)
            k-=1
        
        return temp[0]

        