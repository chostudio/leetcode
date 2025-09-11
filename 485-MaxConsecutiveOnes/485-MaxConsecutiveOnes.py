# Last updated: 9/11/2025, 12:31:47 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, maxim = 0, 0
        for i in nums:
            if i == 1:
                curr += 1
                maxim = max(maxim, curr)
            else:
                curr = 0
        return maxim