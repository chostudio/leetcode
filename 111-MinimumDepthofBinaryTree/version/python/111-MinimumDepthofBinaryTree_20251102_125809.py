# Last updated: 11/2/2025, 12:58:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mini = inf
        if not root:
            return 0
        def dfs(root, height):
            if not root:
                return
            if not root.left and not root.right:
                nonlocal mini
                mini= min(mini, height)
                return
            if root.right:
                dfs(root.right, height + 1)
            if root.left:
                dfs(root.left, height + 1)
            return
        dfs(root, 1)
        return mini