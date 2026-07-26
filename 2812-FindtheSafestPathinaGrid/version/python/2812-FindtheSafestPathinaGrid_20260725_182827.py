# Last updated: 7/25/2026, 6:28:27 PM
1class Solution:
2    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
3        # multi bfs from each thief position to set up the new grid. then bfs from start to finish. O(V+E). edge case where if either start or finish has a thief then just return 0 asap
4        rlen = len(grid)
5        clen = len(grid[0])
6        if grid[0][0] == 1 or grid[rlen-1][clen-1] == 1:
7            return 0
8
9        q = deque()
10        visited = set()
11
12        # loop through and find the thiefs
13        for r in range(rlen):
14            for c in range(clen):
15                if grid[r][c] == 1:
16                    q.append([r, c, 0])
17                    visited.add((r, c))
18        # edit the same matrix
19        while q:
20            r, c, dist = q.popleft()
21            grid[r][c] = dist
22            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
23            for v, h in directions:
24                if 0 <= r + v < rlen and 0 <= c + h < clen:
25                    if (r+v, c+h) not in visited:
26                        visited.add((r+v, c+h))
27                        newdist = dist + 1
28                        q.append([r+v, c+h, newdist])
29
30
31        # remember the trick from rotting orange multi source bfs. you have to mark the "im going to visit node" before you append it into the thing to not double count a thing
32
33        # now do a bfs on it again bc bfs time complexity is V + E. dijstra on other hand is (V+E)logV so dont do that here + we dont need edge weights when bfs can alr visit each node once
34
35        # actually good to remmber when to use each one. BFS gets you shortest path. however, in this scenario, we dont need shortest path. we need smallest value, thus dijstra is what we need bc otherwise the bfs with a visited 2d arr gets TLE bc we can revisit other nodes, its a whole thing
36
37        # bc we need a visited something but we need it to also be possible to 
38        # cell val we've seen at a cell
39        # safestval = [[0] * clen for i in range(rlen)]
40        # value of furthest but max heap, row, col, 
41        h = []
42        heapq.heappush(h, (-grid[0][0], 0,0))
43        # set the cell val of tie first node to itself, special
44        # safestval[0][0] = grid[0][0]
45
46        # dijstra is guanreteed that the first time you see a thing then tahts the biggest/smallest. so we dont nee the 2d arr for visited in this question bc we aint going round and round. just a visited set is enough
47        visited = set()
48        while h:
49            # smallest we've seen is what our takeaway of it is bc its the closest cell that affects safeness
50            # bug: remember, order matters
51            currsafest, r, c  = heapq.heappop(h)
52
53
54            if (r, c) in visited:
55                continue # weve found a safer in the past
56            
57            currsafest = -currsafest
58            visited.add((r, c))
59            if r == rlen - 1 and c == clen - 1:
60                return currsafest # answer
61
62            # else its safer, continue with this path
63            # safestval[r][c] = currsafest
64            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
65            for v, ho in directions:
66                if 0 <= r + v < rlen and 0 <= c + ho < clen:
67                    # you DO NOT need this in the loop dont have this pre pruning line in dijstra
68                    # if currsafest < safestval[r+v][c+ho]:
69                    #     continue
70                    
71                    # mistake: you needed to use [r+v][c+ho] instead of the [r][c]
72                    newsafest = min(currsafest, grid[r+v][c+ho])
73
74                    heapq.heappush(h, (-newsafest, r+v, c+ho))
75        return 0
76        #     # if cellval[r][c] >= smallest:
77        #     #     continue
78        #     # else update it
79        #     smallest = min(grid[r][c], smallest)
80        #     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
81        #     for v, h in directions:
82        #         if 0 <= r + v < rlen and 0 <= c + h < clen:
83        #             if smallest >= cellval[r+v][c+h]:
84        #                 newsmallest = min(grid[r+v][c+h], smallest)
85        #                 cellval[rlen-1][clen-1] = newsmallest
86        #                 q.append([r+v, c+h, newsmallest])
87        # # i lwok forgot how to do bfs, especially the when u "dont need to visit"
88        # return cellval[rlen-1][clen-1]
89            
90
91