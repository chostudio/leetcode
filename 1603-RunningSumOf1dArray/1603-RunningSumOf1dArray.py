# Last updated: 9/11/2025, 12:31:02 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] + nums[i]
        return ans