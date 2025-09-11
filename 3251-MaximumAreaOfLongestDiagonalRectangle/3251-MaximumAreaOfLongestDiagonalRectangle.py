# Last updated: 9/11/2025, 12:30:26 PM
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        diagonal = 0
        for rectangle in dimensions:
            length, width = rectangle
            if sqrt(length * length + width * width) > diagonal:
                diagonal = sqrt(length * length + width * width)
                area = length * width
            elif sqrt(length * length + width * width) == diagonal:
                diagonal = sqrt(length * length + width * width)
                area = max(area, length * width)
        return area