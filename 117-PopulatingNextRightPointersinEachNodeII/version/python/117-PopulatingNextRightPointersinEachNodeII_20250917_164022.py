# Last updated: 9/17/2025, 4:40:22 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        if root is None: # worked but have to have the edge case for what if root is none
            return None

        q = deque([root])

        while q: #
            level = len(q) # 3
            for i in range(level):
                node = q.popleft()
                if i < level - 1: # make sure to minus one. talk out loud helped
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root