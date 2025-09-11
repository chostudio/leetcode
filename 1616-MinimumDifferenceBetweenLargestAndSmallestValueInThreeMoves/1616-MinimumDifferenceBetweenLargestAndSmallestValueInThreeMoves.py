# Last updated: 9/11/2025, 12:31:00 PM
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        val = sys.maxsize
        for l in range(4):
            r= len(nums)- 3 + l
            val = min(val, nums[r-1] - nums[l])
        return val