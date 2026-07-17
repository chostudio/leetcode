# Last updated: 7/16/2026, 7:12:29 PM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        
4        # top down dp with a visited set
5
6        visited = [[inf] * len(grid[0]) for _ in grid]
7        n, m = len(grid), len(grid[0])
8        def dfs(r, c):
9            if 0 <= r <= n - 1 and 0 <= c <= m - 1:
10                # base case is hitting the end or out of bounds
11                if r == n - 1 and c == m - 1:
12                    return grid[r][c]
13                # on a second go around to this exact point, instead of reclaculating we want to just return "hey we calced all the paths from here already, here is the most optimal, take it"
14                if visited[r][c] != inf:
15                    return visited[r][c]
16
17
18                # if not the smallest we've come across at this point, then break off the curr recursion path
19                # currsum += grid[r][c]
20                # if currsum > visited[r][c]:
21                #     return
22                
23                # else currsum <= visited[r][c]:
24                # visited[r][c] = currsum
25                # if in range then go down and go right
26                # continue going back up the chain with the optimal min of the two sums we've seen and the val at this place itself
27                optimalatthispoint = min(dfs(r+1, c), dfs(r, c+1)) + grid[r][c]
28                visited[r][c] = optimalatthispoint
29                return optimalatthispoint
30            else:
31                return inf # inf out of bounds bc we want min so we cant do 0 here
32        return dfs(0,0)
33
34        # return visited[n-1][m-1]
35