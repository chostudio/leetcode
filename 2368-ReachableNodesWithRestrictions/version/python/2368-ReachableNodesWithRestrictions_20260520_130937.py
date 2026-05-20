# Last updated: 5/20/2026, 1:09:37 PM
1class Solution:
2    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
3        adj = defaultdict(list)
4        for a, b in edges:
5            adj[a].append(b)
6            adj[b].append(a)
7        
8        restricted = set(restricted)
9        
10
11        # bfs from 0
12        count = 0
13        visited = set()
14        q = deque([0])
15        while q:
16            node = q.popleft()
17            visited.add(node)
18            count += 1
19            for nei in adj[node]:
20                if nei not in visited and nei not in restricted:
21                    q.append(nei)
22                # you could delete the nei adj list just like jump game 4 but i dont think we would ever revisit the node again so no need
23            
24        return count
25