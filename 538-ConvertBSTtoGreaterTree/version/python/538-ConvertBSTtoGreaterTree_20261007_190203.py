# Last updated: 10/7/2026, 7:02:03 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        globalsum = 0
10        def dfs(root):
11            if not root:
12                return
13                
14            if root.right:
15                dfs(root.right)
16            
17            nonlocal globalsum
18            root.val += globalsum
19            globalsum = root.val
20
21            if root.left:
22                dfs(root.left)
23        
24        dfs(root)
25        return root
26            