# Last updated: 7/11/2026, 4:44:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
9        
10        # tree tp bidirecitonal adj list with diff things inside of the list [next node, U/L/R]
11
12        adj = defaultdict(list)
13
14        def dfs(node):
15            if not node:
16                return
17            if node.left: # each node has unique value
18                adj[node.val].append([node.left.val, "L"])
19                adj[node.left.val].append([node.val, "U"])
20                dfs(node.left)
21            if node.right: # each node has unique value
22                adj[node.val].append([node.right.val, "R"])
23                adj[node.right.val].append([node.val, "U"])
24                dfs(node.right)
25        
26        dfs(root)
27        # print(adj)
28        # bfs shortest with graph
29        visited = set()
30        q = deque()
31        q.append((startValue, ""))
32        while q:
33            node, path = q.popleft()
34
35            if node == destValue:
36                return path
37            
38            visited.add(node)
39            for nei, direction in adj[node]:
40                if nei not in visited:
41                    newpath = path + direction
42                    q.append((nei, newpath))
43        return ""