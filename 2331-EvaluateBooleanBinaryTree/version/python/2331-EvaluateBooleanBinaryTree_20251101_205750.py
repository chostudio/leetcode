# Last updated: 11/1/2025, 8:57:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # post order dfs grab the children nodes and then work tour way bac u with rturn atatments
        def dfs(root):
            if not root.left and not root.right:
                return root.val
            
            left = dfs(root.left)
            right = dfs(root.right)

            if root.val == 2: # or
                if left == 1 or right == 1:
                    return 1
                else:
                    return 0
            if root.val == 3: # and
                if left == 1 and right ==1:
                    return 1
                else:
                    return 0
            # else it's a value T or F
            return root.val
        result = dfs(root)
        return True if result == 1 else False
        
        