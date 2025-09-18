# Last updated: 9/17/2025, 10:44:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, rmin, rmax):
            if not node:
                return True
            # else we hjave a node
            if rmin < node.val < rmax:
                # its good lets continue down
                return dfs(node.left, rmin, node.val) and dfs(node.right, node.val, rmax)
            return False

        return dfs(root, -inf, inf) # we're starting off with the biggest possible range to be safe and shrink it with every level descent