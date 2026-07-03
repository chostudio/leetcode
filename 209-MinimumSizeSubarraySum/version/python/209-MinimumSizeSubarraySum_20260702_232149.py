# Last updated: 7/2/2026, 11:21:49 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        # you can recognize a sligind window when we want to get a length in array. we want to go go go go go until we reach an amount/cap. then shrink shrink shrink left bound while goal coniditon is still met
4        l, r = 0, 0
5        mini = inf
6        curr = 0
7        while r < len(nums):
8            curr += nums[r]
9            while curr >= target:
10                mini = min(mini, r - l + 1)
11                curr -= nums[l]
12                l += 1
13            
14            r += 1
15
16        return mini if mini != inf else 0