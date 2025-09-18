# Last updated: 9/18/2025, 9:26:23 AM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [[1,2,3],[4,5,6],[7,8,9]]
        ans = [] # 1, 2, 3, 6, 9, 8, 7, 4, 5
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) -1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1 # 2
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1 # 0

            if top <= bottom: # WHY IS THIS ONE TOP BOTTOM
                for i in range(right, left -1,  -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1 # 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1 #1
        return ans