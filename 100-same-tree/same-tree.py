# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stackp = [p]
        stackq = [q]
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        while stackp and stackq:

            nodep = stackp.pop()
            nodeq = stackq.pop()

            if nodep.val != nodeq.val:
                return False
            
            if nodep.left and nodeq.left:
                stackp.append(nodep.left)
                stackq.append(nodeq.left)
            elif nodep.left or nodeq.left:
                return False

            if nodep.right and nodeq.right:
                stackp.append(nodep.right)
                stackq.append(nodeq.right)
            elif nodep.right or nodeq.right:
                return False
        return True
