# Last updated: 9/11/2025, 12:32:08 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans += i + 1 - nums[i]
        return ans