# Last updated: 10/20/2025, 6:17:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of max as go down and update and count
        count = 0
        def dfs(root, m):
            if not root:
                return
            nonlocal count
            if m <= root.val:
                count += 1
            m = max(m, root.val)
            dfs(root.left, m)
            dfs(root.right, m)

        dfs(root, -inf)
        return count