# Last updated: 9/11/2025, 12:32:10 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr > target:
                col -= 1
            elif curr < target:
                row += 1
        return False