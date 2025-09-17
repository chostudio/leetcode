# Last updated: 9/16/2025, 5:12:34 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum, maxsum = -inf, -inf
        for i in nums:
            currsum = max(currsum + i, i)
            maxsum = max(currsum, maxsum)
        return maxsum