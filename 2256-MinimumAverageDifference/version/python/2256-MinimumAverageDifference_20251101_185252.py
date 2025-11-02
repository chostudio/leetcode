# Last updated: 11/1/2025, 6:52:52 PM
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)

        runningsum = 0
        index = -1
        smallestavg = inf
        for i in range(len(nums)):
            runningsum += nums[i] 
            # had a plus instea of minus
            divisor = i + 1
            # round down avg
            amount = abs(runningsum//divisor - (totalsum-runningsum)//(n-divisor)) if i < n-1 else runningsum/divisor
            # cannot divide by 0
            if amount < smallestavg:
                smallestavg = amount
                index = i
        return index