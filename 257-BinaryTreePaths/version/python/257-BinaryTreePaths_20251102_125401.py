# Last updated: 11/2/2025, 12:54:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # oh any node that has no children works lol. makes it easier else wouldnve dfs for max height first
        if not root:
            return
        if not root.right and not root.left:
            return [str(root.val)] # if only one

        def dfs(root, arr):
            if not root:
                return
            # root exists now
            arr.append(str(root.val)) # turn int into string
            
            if root.left:
                dfs(root.left, arr.copy()) # must pass by value not reference so we make a new arr in python bc otherwise we would be editing the same arr in every recusrive call whichis not right
            if root.right:
                dfs(root.right, arr.copy())

            if not root.left and not root.right: # forgot the second "not" typo
                nonlocal ans
                ans.append("->".join(arr)) # makes a copy/string of the arr with -> as teh inbetween thingy
            return
        

        ans = []
        dfs(root, [])
        return ans
