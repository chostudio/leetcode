# Last updated: 9/11/2025, 12:32:17 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 10**9
        l, r = 0, 0
        currAmount = 0
        while r < len(nums):
            currAmount += nums[r]
            while currAmount >= target:
                length = min(length, r - l + 1)
                currAmount -= nums[l]
                l += 1
            r += 1
        return length if length != 10**9 else 0