# Last updated: 3/12/2026, 10:58:02 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        oneback, twoback = 0,0
4        for curr in nums:
5            temp = oneback
6            if twoback + curr > oneback:
7                oneback = twoback + curr
8            twoback = temp
9
10        return oneback
11