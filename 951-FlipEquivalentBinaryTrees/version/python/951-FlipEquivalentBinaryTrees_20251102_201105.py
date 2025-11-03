# Last updated: 11/2/2025, 8:11:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True # reached the end
            if root1 and not root2:
                return False
            if not root1 and root2:
                return False # if one exists but the other doesnt then not correct
            # there is something there
            if root1.val != root2.val:
                return False
            # otherwise keep going by calling the children and swapping them bc it could be either case that is possibly true
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right) or dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        return dfs(root1, root2)