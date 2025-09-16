# Last updated: 9/15/2025, 4:06:46 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r] # overwrite
            r += 1
        return l + 1