# Last updated: 10/26/2025, 10:46:54 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()

        def dfs(root):
            if not root:
                return False
            
            if k - root.val in hashset:
                return True
            hashset.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)