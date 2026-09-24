# Last updated: 9/23/2026, 5:06:56 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: TreeNode | None) -> int:
9        
10        ans = 0
11
12        def dfs(node, pathsum):
13            if not node:
14                return
15            
16            pathsum *= 10
17            pathsum += node.val
18        
19            if not node.right and not node.left:
20                nonlocal ans
21                ans += pathsum
22                return
23            
24            dfs(node.left, pathsum)
25            dfs(node.right, pathsum)
26        
27        dfs(root, 0)
28        return ans