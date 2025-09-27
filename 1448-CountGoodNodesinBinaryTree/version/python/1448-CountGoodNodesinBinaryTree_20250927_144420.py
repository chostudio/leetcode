# Last updated: 9/27/2025, 2:44:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs and pass the max val u encounte obn th epath, start the var at -inf then update with root val, += 1 every time to global var (arr element) or nonlocal

        ans = [0]
        def dfs(root, biggest):
            if not root:
                return
            if biggest <= root.val:
                ans[0] += 1
                biggest = root.val
            dfs(root.left, biggest) # accidentally called the g func instead of dfs
            dfs(root.right, biggest)
        dfs(root, -inf)
        return ans[0]