# Last updated: 9/11/2025, 12:30:20 PM
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # i actually got the right intuition. just find the top, bottom, right, left most points of 1s and store them in 4 variables and then calculate multiply for final answer of rectangle size hooray
        #start on opposite sides
        top = 0
        bottom = len(grid) -1
        left = len(grid[0]) -1
        right = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                value = grid[r][c]
                if value ==1:
                    # NOT comparing to the valuee, but the indexes
                    top = max(top, r)
                    bottom = min(bottom, r)
                    left = min(left, c)
                    right = max(right, c)
        # l * w. if on top of each other, cannot be 0 o + 1            
        return (right - left + 1) * (top - bottom + 1)