# Last updated: 9/27/2025, 11:43:42 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        #bfs and just app last val in q
        q = deque([root])
        ans =[]
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == length - 1: # not len(q) bc that changes every pop
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
