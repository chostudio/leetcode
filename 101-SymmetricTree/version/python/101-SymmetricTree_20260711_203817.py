# Last updated: 7/11/2026, 8:38:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        
10        def dfs(node1, node2):
11            if not node1 and not node2:
12                return True # leaf
13            
14            # if node1.left and not node2.right or node1.right and not node2.left:
15            #     return False
16            # we have the double false case above, thus if one of them gone, then this will be false
17            if not node1 or not node2:
18                return False
19
20            # now assume that both nodes exist, and thus can check the val
21            if node1.val != node2.val:
22                return False
23
24            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
25        
26        return dfs(root.left, root.right) if root else False