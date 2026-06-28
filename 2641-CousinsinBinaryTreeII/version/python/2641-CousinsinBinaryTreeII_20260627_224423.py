# Last updated: 6/27/2026, 10:44:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        # Two nodes of a binary tree are cousins if they have the same depth with different parents. so im kinda thinking bfs level order starting on level 3 and continue or dfs but you just check two below and add them together and set them 
10        depth = 0
11        copy = root
12        q = deque()
13        q.append((root, 0))
14
15        # when you append, you also need to pass in the value of the sibling and itself node to minus it from total
16        while q:
17            length = len(q)
18            total = 0
19            # add up, without popping or adding
20            if depth > 0:
21                for i in range(length):
22                    total += q[i][0].val
23            for _ in range(length):
24                # print(q[0])
25                node, oldsiblings = q.popleft()
26                node.val = total - oldsiblings
27                siblings = 0
28                if node.left:
29                    siblings += node.left.val
30                if node.right:
31                    siblings += node.right.val
32                if node.left:
33                    q.append((node.left, siblings))
34                if node.right:
35                    q.append((node.right, siblings))
36            depth += 1
37        
38        return copy