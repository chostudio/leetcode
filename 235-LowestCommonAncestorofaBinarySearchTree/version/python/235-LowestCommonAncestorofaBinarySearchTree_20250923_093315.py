# Last updated: 9/23/2025, 9:33:15 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we specifically rely on the properties of a BST (not just a regular binary tree, which is not always sorted like a BST) anything left of a node is smaller, anything right is bigger.

        # we can assume nodes p and q will exist as per the contraints. (what to do if they didnt?) So if we encounter a node that isn't 
        if not root: #  ???not p or not q: or
            return 
        # if both values are less than the curr node, then we must traverse left
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # else if, both values are bigger than curr node, then we must go right
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # else, there is one value greater than this node and one smaller, so we found our LCA at this root since this is where the values split and will eventually meet up
        else:
            return root