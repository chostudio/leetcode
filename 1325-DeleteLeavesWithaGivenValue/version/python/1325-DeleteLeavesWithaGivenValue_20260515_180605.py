# Last updated: 5/15/2026, 6:06:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
9        # post order bc parent needs to be the one to remove child
10        def dfs(node):
11            if not node:
12                return
13            
14            left = dfs(node.left) if node.left else None
15            right = dfs(node.right) if node.right else None
16
17            # resubmitted. remember that it's only leaf nodes, so we have to check if the child node is a leaf before removing it if it. meets the conditions
18            if left and left.val == target and left.left is None and left.right is None:
19                node.left = None
20            if right and right.val == target and right.left is None and right.right is None:
21                node.right = None
22            
23            
24            return node
25        
26        dfs(root)
27        # edge case where if the root is the value and is a leaf
28        return None if root and root.val == target and root.left is None and root.right is None else root
29