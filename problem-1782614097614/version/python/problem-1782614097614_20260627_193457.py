# Last updated: 6/27/2026, 7:34:57 PM
1class Solution:
2    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
3        nums.sort(reverse=True)
4        ans = 0
5        for i in range(k):
6            val = nums[i]
7            if val * mul > val:
8                ans += val * mul
9            else:
10                ans += val
11            mul -= 1
12        return ans