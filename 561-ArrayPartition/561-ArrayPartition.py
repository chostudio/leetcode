# Last updated: 9/11/2025, 12:31:43 PM
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(len(nums)-2,-1, -2):
            s += nums[i]
        return s