# Last updated: 10/6/2025, 4:05:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # actually uses a helper function that is the same as is same tree wrapped lol
        def sametree(n1, n2):
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (not n1 and n2):
                return False
            if n1.val != n2.val:
                return False
            return sametree(n1.left, n2.left) and sametree(n1.right, n2.right)
        
        if not root and not subRoot:
            return True
        
        if not root: # if we go all the way down return false, if there is one true it will offset it
            return False
        
        if root.val == subRoot.val and sametree(root, subRoot) == True:
            return True

        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                