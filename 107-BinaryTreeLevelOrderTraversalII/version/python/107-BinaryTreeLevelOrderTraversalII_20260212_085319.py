# Last updated: 2/12/2026, 8:53:19 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root: return []
10        q = deque([root])
11        ans = []
12        while q:
13            length = len(q)
14            level = []
15            for _ in range(length):
16                node = q.popleft()
17                level.append(node.val)
18                if node.left:
19                    q.append(node.left)
20                if node.right:
21                    q.append(node.right)
22            ans.append(level)
23        # you can maybe pushleft deque and return deque but to be safe, use array
24        ans.reverse()
25
26        return ans
27