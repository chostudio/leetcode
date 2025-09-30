# Last updated: 9/29/2025, 5:25:09 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r] # overwriting
                l += 1
            r += 1
        return l # usually 0 index so plus 1 but not in this way how we wrote it ig