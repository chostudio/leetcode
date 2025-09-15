# Last updated: 9/14/2025, 7:09:45 PM
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs. and apprently if you do it with a bfs then the part 2 question is the exact same solution?
        from collections import deque 
        if root is None:
            return
        queue = deque([root]) # putting the root node into a list then changing that list into a deque. or could just append it after init the deque
        while queue:
            length = len(queue)
            for i in range(length):
                # regardless of last, make sure ot pop it
                node = queue.popleft()
                if i < length - 1: # aka not the last node so make it point right
                    node.next = queue[0] # point to the next node in the queue which is the node most rightmost to it
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root # even though doesnt specifiy u need to retunr root you do
