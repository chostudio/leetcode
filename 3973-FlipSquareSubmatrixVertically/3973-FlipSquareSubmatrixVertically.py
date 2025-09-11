# Last updated: 9/11/2025, 12:30:15 PM
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # two pointer
        # but also need to make sure that you dont go out of bounds. not guarenteeed k will be so you need to choose min of legnth or k
        end = min(y + k, len(grid[0])) # u dont need the -1 here since the while loop is a < so it'll end off before oobounds
        while y < end:
            # ohhhhhh my god it's a K sized square, not all the way to the bottom. have to reread the question
            top, bottom = x, min(x + k-1, len(grid)-1)
            while top <= bottom:
                # swap
                print(grid[top][y], grid[bottom][y])
                grid[top][y], grid[bottom][y] = grid[bottom][y], grid[top][y]
                top +=1
                bottom -=1
            y += 1
        return grid