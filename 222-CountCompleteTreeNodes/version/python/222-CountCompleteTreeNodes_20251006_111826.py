# Last updated: 10/6/2025, 11:18:26 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # i guess we're just counting nodes. nothing special to it since we're guarenteed to have a COMPLETE (every level is filled except for the last) binary tree
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1