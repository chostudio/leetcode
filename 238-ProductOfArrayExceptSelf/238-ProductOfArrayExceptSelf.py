# Last updated: 9/11/2025, 12:32:11 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] *= prefix
            ans[-i-1] *= postfix
            prefix *= nums[i]
            postfix *= nums[-i-1]
        return ans
