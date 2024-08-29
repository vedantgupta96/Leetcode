"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        start = node
        stack = [start]
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            oldToNew[node] = Node(val=node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        for oldNode,newNode in oldToNew.items():
            for nei in oldNode.neighbors:
                new_nei = oldToNew[nei]
                newNode.neighbors.append(new_nei)
        return oldToNew[start]


        
        
        