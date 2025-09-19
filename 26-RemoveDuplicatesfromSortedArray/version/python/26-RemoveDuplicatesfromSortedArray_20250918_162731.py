# Last updated: 9/18/2025, 4:27:31 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,2,_]
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1