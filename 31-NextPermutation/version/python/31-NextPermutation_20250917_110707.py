# Last updated: 9/17/2025, 11:07:07 AM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # right to left find smaller number (bc that be pivot point)
        i = len(nums) -1
        while i > 0 and nums[i - 1] >= nums[i]: #
            i -= 1
        # i - 1 is the number that is smaller than the numbers to the right
        if i == 0: # went through entire arr and nothing
            return nums.reverse()
        
        j = len(nums) -1
        while j > i and nums[j] <= nums[i-1]: # bigger number # i - 1 for second part bc focus on swap the pivot point
            j -= 1
        
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        l, r = i, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums
