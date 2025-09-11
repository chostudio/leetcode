# Last updated: 9/11/2025, 12:31:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def dfs(root):
            if root is None:
                return 0
            nonlocal diam
            left = dfs(root.left)
            right = dfs(root.right)
            diam = max(diam, left + right)
            return max(left, right) + 1
        dfs(root)
        return diam