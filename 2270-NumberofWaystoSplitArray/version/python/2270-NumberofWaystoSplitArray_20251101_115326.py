# Last updated: 11/1/2025, 11:53:26 AM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # assuming prefix sum and running sum
        total = sum(nums)
        splits = 0
        running = 0
        for r in range(len(nums)-1): # we cannot access last index
            running += nums[r]
            if running >= total - running:
                splits += 1
        return splits