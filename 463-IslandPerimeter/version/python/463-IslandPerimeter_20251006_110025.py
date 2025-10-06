# Last updated: 10/6/2025, 11:00:25 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for r in range(len(grid)):
            for c in range(len(grid[0])): # FORGOT THE ZERO UGHHH
                if grid[r][c] == 1:
                    # do it up to four times
                    for row, col in dir:
                        # if OOB or 0
                        if 0 > r + row or r + row >= len(grid) or 0 > c + col or c + col >= len(grid[0]):
                            perimeter += 1
                        elif grid[r + row][c + col] == 0:
                            perimeter += 1
        return perimeter