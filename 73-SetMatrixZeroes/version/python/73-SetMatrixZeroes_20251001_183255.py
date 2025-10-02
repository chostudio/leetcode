# Last updated: 10/1/2025, 6:32:55 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we gonna store 0 in 0th row and col. check to make sure if any 0 in 0th row or col first and store them
        zerorow = False
        zerocol = False
        for i in matrix[0]:
            if i == 0:
                zerorow = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zerocol = True
        
        # now iterate through regular 2d array and set 0s in 0th row and col
        # also need to make sure we dont iterate through 0th row and col again
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # now 0 are in place in the 0th row and col
        # need to remember to skip the 0,0 index otherwise it would change th 0th row and col to all 0s
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                # then change column into 0
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        # need to remember to skip the 0,0 index otherwise it would change th 0th row and col to all 0s
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                # then change row into 0
                for c in range(1, len(matrix[0])):
                    matrix[r][c] = 0
        
        if zerorow == True:
            for r in range(len(matrix[0])):
                matrix[0][r] = 0

        if zerocol == True:
            for c in range(len(matrix)):
                matrix[c][0] = 0
               