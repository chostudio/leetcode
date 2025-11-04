# Last updated: 11/3/2025, 10:12:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal add to an array then get kth -1 index?
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # nonlocal arr
            arr.append(root.val)
            dfs(root.right)
            return
        dfs(root)
        return arr[k-1]