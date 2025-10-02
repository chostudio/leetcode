# Last updated: 10/1/2025, 8:20:03 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap along diagonal
        for r in range(len(matrix)):
            # c would be 0, then 1, then 2
            # only along the diagonal bc if you were to iterate thorugh entire aray it would literally just be the same thing
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r],matrix[r][c]
        
        for row in matrix:
            row.reverse()
        