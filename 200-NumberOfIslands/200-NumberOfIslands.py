# Last updated: 9/11/2025, 12:32:20 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        # changes recursively the 1s into zeros
        def dfs(rowIndex, colIndex):
            if rowIndex >= len(grid) or rowIndex < 0 or colIndex >= len(grid[0]) or colIndex < 0 or grid[rowIndex][colIndex] != "1":
                return
            grid[rowIndex][colIndex] = "0"
            dfs(rowIndex+1, colIndex)
            dfs(rowIndex-1, colIndex)
            dfs(rowIndex, colIndex+1)
            dfs(rowIndex, colIndex-1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count