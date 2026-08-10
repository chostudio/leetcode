# Last updated: 8/9/2026, 7:55:49 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        # mst prims. in this case it is not sorted so we will have to build it AS WE GO ALONG, not all at the beginning. 
4        # regardless, O(n^2) time complexity at the worst
5        # prims uses a heap
6
7        heap = []
8        costs = [10000000] * len(points) # instead of having to worry about connecting all components and worrying about edge count, we simplify the thought by going okay, whats the smallest edge to get to this point. because by doing so there should be at least one edge - 1 for all points
9        # costs[0] = 0 # cost to get to the first node is 0, that is our edges = nodes - 1
10
11        # cost to get there, [x, y]
12        heapq.heappush(heap, (0, points[0], 0))
13        visited = set()
14        while heap:
15            cost, point, index = heapq.heappop(heap)
16            x, y = point
17            # print(cost, x, y, index)
18
19            if (x, y) in visited: continue
20            # if costs[index] <= cost: continue
21
22            costs[index] = cost # basically our visited set
23            visited.add((x, y))
24
25            for i in range(len(points)):
26                nx, ny = points[i]
27                if index == i: continue
28                if (nx, ny) in visited: continue
29                # if nx == x and ny == y: continue # same point
30
31                manhat = abs(x - nx) + abs(y - ny)
32                # if we've already found a cheaper way, then dont bother trying this way
33                # if costs[i] <= manhat: continue
34
35                heapq.heappush(heap, (manhat, points[i], i))
36            
37        # print(costs)
38        return sum(costs)