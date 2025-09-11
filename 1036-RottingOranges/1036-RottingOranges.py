# Last updated: 9/11/2025, 12:31:20 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        freshOranges = 0
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshOranges += 1
                elif grid[r][c] == 2:
                    # the index of where the rotten thing is
                    queue.append((r, c))
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]] # makes it way easier to go up, left, right, down
        days = 0
        # now we have num of fresh oranges and rotten ones
        while queue and freshOranges > 0:
            # bfs uses length lol dont forget
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()
                # turn neighbors rotten
                for i, j in directions:
                    if 0 <= row + i <= len(grid) -1 and 0 <= col + j <= len(grid[0]) -1 and grid[row + i][col + j] == 1: # check to amke sure its not rotten already. HAS TO BE EQUAL TO ONEEEEE not two
                        queue.append((row + i, col + j))
                        # i think you need to change the value of the cell to be 2? so that other cells dont accidentally reappend the same cell
                        grid[row + i][col + j] = 2
                        freshOranges -= 1
            days += 1
        return days if freshOranges == 0 else -1
