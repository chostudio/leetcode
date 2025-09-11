# Last updated: 9/11/2025, 12:31:40 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currSum = sum(nums[0:k])
        for i in range(k, len(nums)):
            currSum = currSum -nums[i-k]+nums[i] 
            # always slide the window to  keep track of the current sliding window.
            # max sum only keeps track of the max window
            maxSum = max(maxSum, currSum)
        return maxSum / k