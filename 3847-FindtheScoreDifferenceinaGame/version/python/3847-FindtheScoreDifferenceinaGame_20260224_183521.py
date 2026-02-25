# Last updated: 2/24/2026, 6:35:21 PM
1class Solution:
2    def scoreDifference(self, nums: List[int]) -> int:
3        a, b = 0, 0
4        swapcount = 0
5        for i in range(len(nums)):
6            if ( i + 1 )% 6 == 0:
7                a, b = b, a
8                swapcount += 1
9            if nums[i] % 2 != 0:
10                a, b = b, a
11                swapcount += 1
12            a += nums[i]
13        
14        return a - b if swapcount % 2 == 0 else b - a