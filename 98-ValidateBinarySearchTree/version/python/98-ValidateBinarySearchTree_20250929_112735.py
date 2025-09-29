# Last updated: 9/29/2025, 11:27:35 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # it's a range
        def dfs(root, maxV, minV):
            if not root:
                return True
            # now we have a root for sure so lets check value if valid
            # make sure you double check the operators
            if root.val <= minV or root.val >= maxV: # cannot be equal or out of range
                return False
            
            # else it's good so keep on going down
            # if go left then the curr node needs to be greater than leftwards, else right, curr node val needs to be smaller than all
            # if defined inside of function, then no need self.
            return dfs(root.left, root.val, minV) and dfs(root.right, maxV, root.val)
            # has to be 'and' bc entire tree needs to be valid
            # dunno if both left and right so you need to check first. actually u dont need to check bc even if itll return accordingly
        return dfs(root, inf, -inf)