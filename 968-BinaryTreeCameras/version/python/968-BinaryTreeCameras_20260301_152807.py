# Last updated: 3/1/2026, 3:28:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    cameras = 0
9
10    def minCameraCover(self, root: Optional[TreeNode]) -> int:
11        # 0 leaf node, not covered obviously
12        # 1 covered, is a camera
13        # 2 covered, but no camera
14        
15        def dfs(node):
16            if not node:
17                return 2
18            l, r = dfs(node.left), dfs(node.right)
19            # if either is a leaf (not covered value)
20            if l == 0 or r == 0:
21                self.cameras += 1
22                return 1
23            # We've taken care of the not covered value above. We are guaranteed now that both children are covered or have a camera. Now we debate between the last two to decide fate of current node needing
24
25            if l == 1 or r == 1: # if either is camera then we good
26                return 2
27            # thus, if neither is a camera but they are covered, we don't need to create a camera for them BUT we would return that I am not covered 
28            return 0
29        return self.cameras + 1 if dfs(root) == 0 else self.cameras