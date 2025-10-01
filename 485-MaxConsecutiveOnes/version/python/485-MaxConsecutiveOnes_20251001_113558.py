# Last updated: 10/1/2025, 11:35:58 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        currcount = 0
        for num in nums:
            if num == 1:
                currcount += 1
                maxones = max(currcount, maxones)
            else: # it's a 0 the adj one counter is no more
                currcount = 0
        return maxones