# Last updated: 3/5/2026, 8:48:23 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        twoback, oneback = 0, 0
4        for i in range(len(nums)):
5            temp = oneback
6            # shift forward the first one first to the next one
7            oneback = max(oneback, twoback + nums[i])
8            twoback = temp # shift forward twoback to one back
9        
10        return oneback # will always have oneback as the max answer bc it was the most recently updated one with the max function