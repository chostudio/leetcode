# Last updated: 9/11/2025, 12:31:06 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        candyAmount = max(candies) - extraCandies
        for i in candies:
            if i >= candyAmount:
                result.append(True)
            else:
                result.append(False)
        return result