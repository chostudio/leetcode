# Last updated: 9/11/2025, 12:32:05 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ab = abs(nums[i])
            if nums[ab] < 0: # negative
                return ab # means that we've already visited it, duplicate
            nums[ab] = -nums[ab] # negating it