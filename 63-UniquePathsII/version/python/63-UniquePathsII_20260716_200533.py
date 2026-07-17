# Last updated: 7/16/2026, 8:05:33 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
3        # you go down the thing if you hit a thing then you just return 0 from it. else calc both and if we hit same again then just returned combined
4        m, n = len(obstacleGrid), len(obstacleGrid[0])
5        visited = [[-1] * n for i in range(m)]
6        def dfs(r, c):
7            if r < 0 or r >= m or c < 0 or c >= n:
8                return 0 # oob
9            # else in bounds, 
10            if visited[r][c] != -1: # -1 means we havent seen it, cannot init to 0 bc that s valid answer
11                return visited[r][c]
12            if obstacleGrid[r][c] == 1: # obstacle
13                return 0 # cannot go here
14            # forgot the basecase, obv. if we reach the end then that's +1, if we never make it then nah
15            if r == m-1 and c == n-1:
16                return 1 # one count
17
18            # else first time we've seen it, must traverse and calc. from rigth we can do this many, from down we can do this many
19            pathsfromthispoint = dfs(r+1, c) + dfs(r, c+1)
20            visited[r][c] = pathsfromthispoint
21            return pathsfromthispoint
22        return dfs(0,0)