# Last updated: 9/11/2025, 12:31:35 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0

        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0
            
            # else it must be an accessible cell
            if grid[row][col] != 1:
                return 0 # otherwise it's a 0 or visited and we don't do nothing
            # mark as visited. just not 1 or 0
            grid[row][col] = 2
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(dfs(i, j), count)

        return count
