# Last updated: 10/6/2025, 4:25:59 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return # dont forget the null nodes after leaf nodes case
            for child in root.children:
                dfs(child)
            ans.append(root.val) # dont put this in the for loop
        dfs(root)
        return ans