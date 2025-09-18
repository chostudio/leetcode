# Last updated: 9/17/2025, 5:05:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root is None:
            return [] # have to reutrn empty bracket not none in python
        q = deque([root])

        ans = []
        while q: #
            length = len(q) # 2
            temp = []
            for i in range(length):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans
