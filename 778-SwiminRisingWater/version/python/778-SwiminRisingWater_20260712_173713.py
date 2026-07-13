# Last updated: 7/12/2026, 5:37:13 PM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        # is it dijstra smallest but then you are also checking for elgitmately anyway works during that as long as we can move, and then if we can reach end then return the current depth of water
4
5        # we could do O(t) 0->t linearly buttt couldn't we lwok binary search on the t to see if possible? dfs/bfs every path with a visited, if less than t then we good. 0-max in grid is the bounds of t but t it self is small so you could but prolly not worth it?
6
7        heap = []
8        heapq.heappush(heap, (0,0,0))
9        # cant reacht the last point or start point if the water isnt at that level so at a minimum, it will be from that time
10        t = max(grid[0][0], grid[len(grid)-1][len(grid[0])-1])
11        visited = set()
12        visited.add((0,0))
13        # either we get to the end or if cannot go any more then t incremenets. there wouldn't be a infinite
14        while heap:
15            while heap and heap[0][0] <= t:
16                val, r, c = heapq.heappop(heap)
17                if r == len(grid)-1 and c == len(grid[0])-1:
18                    return t
19                # 4 directions from this point
20                # in bounds, value less than t--no we gotta add it anyways, just make sure its not visited set alr
21                if r - 1 >= 0 and (r-1, c) not in visited:
22                    visited.add((r-1, c))
23                    heapq.heappush(heap, (grid[r-1][c], r-1, c))
24                if r + 1 <= len(grid)-1 and (r+1, c) not in visited:
25                    visited.add((r+1, c))
26                    heapq.heappush(heap, (grid[r+1][c], r+1, c))
27
28                if c - 1 >= 0 and (r, c-1) not in visited:
29                    visited.add((r, c-1))
30                    heapq.heappush(heap, (grid[r][c-1], r, c-1))
31
32                if c + 1 <= len(grid[0])-1 and (r, c+1) not in visited:
33                    visited.add((r, c+1))
34                    heapq.heappush(heap, (grid[r][c+1], r, c+1))
35
36                
37            
38            t += 1
39
40
41
42            