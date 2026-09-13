# Last updated: 9/13/2026, 10:19:23 AM
1class Solution:
2    def findMaxFish(self, grid: List[List[int]]) -> int:
3        # basically flood fill dfs from every point if we havnet visited it and return biggest total
4
5        # as we traverse and visit cell group, we mark as visited by changing cell into 0. alternative would be to have another grid we make act as a visited true or false check if we didnt want to mutate OG grid
6        def dfs(r, c):
7            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
8                return 0 # out of bounds
9            if grid[r][c] == 0:
10                return 0
11            
12            result = grid[r][c]
13            grid[r][c] = 0 # erseae it to not visit again BEFORE traverseing
14            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
15            for a, b in directions:
16                newr = r + a
17                newc = c + b
18                if newr < 0 or newr >= len(grid) or newc < 0 or newc >= len(grid[0]):
19                    continue
20                result += dfs(newr, newc)
21            
22            return result
23            
24        ans = 0
25        for r in range(len(grid)):
26            for c in range(len(grid[0])):
27                if grid[r][c] != 0:
28                    ans = max(ans, dfs(r, c))
29
30
31        return ans