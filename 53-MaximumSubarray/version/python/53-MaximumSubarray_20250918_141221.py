# Last updated: 9/18/2025, 2:12:21 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = -inf, -inf
        # 5, 6
        # [-2,1,-3,4,-1,2,1,-5,4]

        for i in nums:
            currSum = max(i , i + currSum)
            maxSum = max(maxSum, currSum)
        return maxSum