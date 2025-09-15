# Last updated: 9/14/2025, 7:13:42 PM
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
        if not root:
            return
        from collections import deque
        q = deque([root])

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i < length - 1: # not the last value
                    node.next = q[0] # the next value in the queue is to the right
                #make sure it's left then right
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right) 
        return root