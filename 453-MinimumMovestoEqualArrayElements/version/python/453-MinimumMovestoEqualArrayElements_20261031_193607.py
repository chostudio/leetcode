# Last updated: 10/31/2026, 7:36:07 PM
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        # work the other way around. incrementing all except one is the same as decrementing only one. we can only decrement one number at a time. (never incrementing) so the number of jumps is the value between the biggest and smallest numbers
4        big, small = -inf, inf
5        for num in nums:
6            if num > big:
7                big = num
8            if num < small:
9                small = num
10        # second pass is all the numbers, how many times between it and smallest difference
11        total = 0
12        for num in nums:
13            total += abs(num - small)
14        return total