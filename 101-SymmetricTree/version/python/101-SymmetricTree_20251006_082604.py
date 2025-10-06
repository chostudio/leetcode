# Last updated: 10/6/2025, 8:26:04 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(n1, n2):
            if not n1 and not n2:
                return True
            # bc we've already covered the case where niether exists. so if one exists but the other doesnt then false
            if not n1 or not n2:
                return False
            # now both exists
            if n1.val != n2.val:
                return False
            
            return mirror(n1.left, n2.right) and mirror(n1.right, n2.left)
        
        return mirror(root.left, root.right)