# Last updated: 9/23/2026, 3:39:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
9        
10        def dfs(root1, root2):
11            # assume root1 and root 2 node exist
12            if not root1.left and not root2.left and not root1.right and not root2.right:
13                return # no children
14
15            if root1.left and root2.left:
16                root1.left.val = root1.left.val + root2.left.val
17                dfs(root1.left, root2.left)
18
19            if root2.left and not root1.left:
20                root1.left = root2.left
21            
22            if root1.right and root2.right:
23                root1.right.val = root1.right.val + root2.right.val
24                dfs(root1.right, root2.right)
25            
26            if root2.right and not root1.right:
27                root1.right = root2.right
28        
29        if not root1: return root2
30        if not root2: return root1
31        root1.val = root1.val + root2.val
32        dfs(root1, root2)
33        return root1