# Last updated: 9/17/2025, 10:35:45 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == "1":
                    grid[r][c] = "2"
                    dfs(r, c+1)
                    dfs(r, c-1)
                    dfs(r-1, c)
                    dfs(r+1, c)
            return # if hit a 0 or 2 then return
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
