# Last updated: 4/29/2026, 10:13:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        maxmax = -inf # guarenteed that there is at least 1 node
10        def dfs(node):
11            if not node:
12                return 0
13            # node exists and now has a value
14            
15            left = max(0, dfs(node.left) if node.left else 0)
16            right = max(0, dfs(node.right) if node.right else 0)
17            nonlocal maxmax
18            maxmax = max(maxmax, left + node.val + right)
19            return node.val + max(left, right) # we can only pick one path
20
21        dfs(root)
22        return maxmax