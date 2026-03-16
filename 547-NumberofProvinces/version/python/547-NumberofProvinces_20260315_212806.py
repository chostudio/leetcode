# Last updated: 3/15/2026, 9:28:06 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        
4        
5        count = 0
6        # bfs
7        visited = set()
8        def bfs(i):
9            nonlocal visited
10            
11            q = collections.deque([i])
12            while q:
13                node = q.popleft()
14                visited.add(node)
15                # going through neighbors, but the 2d adj matrix is only in 0 and 1 so it's the index that matters
16                for index, val in enumerate(isConnected[node]):
17                    if val == 1 and index not in visited:
18                        q.append(index)
19        
20        for i in range(len(isConnected)):
21            if i not in visited:
22                bfs(i)
23                count += 1
24        return count