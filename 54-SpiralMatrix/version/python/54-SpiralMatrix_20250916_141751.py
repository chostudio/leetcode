# Last updated: 9/16/2025, 2:17:51 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            # bc we move top and right there is possiblity that it wouldnt work rn so we need to have if sattement to check before w e do it
            if top <= bottom: # if still valid bc possiblity it is not
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            if left <= right: #both of them are minus -1 here bc it's exclusive so you'll be fine. both are -1 bc we need to go in reverse order traversing from biggest to smaller values
                for r in range(bottom, top -1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans