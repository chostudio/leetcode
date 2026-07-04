# Last updated: 7/3/2026, 9:16:59 PM
1class Solution:
2    def minScore(self, n: int, roads: List[List[int]]) -> int:
3        adj = defaultdict(list)
4
5        for a, b, dist in roads:
6            adj[a].append((b, dist))
7            adj[b].append((a, dist))
8        
9        heap = []
10        heapq.heappush(heap, (10**5, 1))
11        visited = [inf] * (n + 1)
12        ans = inf
13        while heap:
14            smallestsofar, node  = heapq.heappop(heap)
15            # smallestsofar = min(smallestsofar, )
16            
17            if visited[node] > smallestsofar:
18                visited[node] = smallestsofar
19            else:
20                continue
21            
22            if node == n:
23                ans = min(ans, smallestsofar)
24                # continue
25
26            for nei, newdist in adj[node]:
27                newsmallest = min(smallestsofar, newdist)
28                heapq.heappush(heap, (newsmallest, nei))
29        return ans