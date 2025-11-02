# Last updated: 11/2/2025, 8:53:44 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # possible to dfs whenever you find a new value and update global var but since recursion alr use space might as well hashmap counter then find at end
        freq = defaultdict(int)
        maxfreq = 0
        
        def dfs(root):
            if not root:
                return
            freq[root.val] += 1
            nonlocal maxfreq # must nonlocal in order to access it
            maxfreq = max(maxfreq, freq[root.val])
            dfs(root.right)
            dfs(root.left)
            return
        dfs(root) # u forgot to call the func lmao
        ans =[]
        # enumerate gets index remember we dont need that
        for key, val in freq.items():
            print(key, val)
            if val == maxfreq:
                ans.append(key)
        return ans
