# Last updated: 9/11/2025, 12:30:44 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = inf
        for i in nums:
            if abs(i) < abs(close):
                close = i
            elif abs(i) == abs(close):
                close = max(i, close)
        return close