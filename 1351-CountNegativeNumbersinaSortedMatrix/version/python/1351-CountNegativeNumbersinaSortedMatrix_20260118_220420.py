# Last updated: 1/18/2026, 10:04:20 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        # bin search to find the last 0 value. then math to calc how many neg numbers there are to the right of it and to the bottom of it. however, much easier way would be to do linear search
4        count = 0
5        for r in range(len(grid)):
6            for c in range(len(grid[0])):
7                if grid[r][c] < 0: count += 1
8        return count