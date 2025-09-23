# Last updated: 9/23/2025, 12:41:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # different than just a normal binary tree. values are whereever. so you need to find where the left and right nodes are. then as we traverse back up we keep on returning what the left or right node was and when we eventually hit a curr node that has the values of the left and right filled in then it must be the LCA so return the curr node
        # could also combine these first two statements
        # check if the curr node exists
        if not root:
            return
        if root == p or root == q:
            return root
        
        # if not the right ones then we need to continue finding the p and q values
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: # oh we have both of the nodes so this must be where they meet
            return root
        
        # if left exists, then return left. if right exists, then return right (python shorthand syntax)
        return left or right

        