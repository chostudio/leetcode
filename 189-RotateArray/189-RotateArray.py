# Last updated: 9/11/2025, 12:32:22 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1
        k = k % len(nums)
        # reverse the entire num arr
        reverse(0, len(nums)-1)
        # reverse the before k part
        reverse(0, k-1)
        # reverse the after k part
        reverse(k, len(nums)-1)
        