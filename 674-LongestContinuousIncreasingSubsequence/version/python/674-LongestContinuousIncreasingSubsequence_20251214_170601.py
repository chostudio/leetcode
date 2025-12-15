# Last updated: 12/14/2025, 5:06:01 PM
1class Solution:
2    def findLengthOfLCIS(self, nums: List[int]) -> int:
3        l, r = 0, 1
4        if len(nums) == 1:
5            return 1
6        longest = 0
7        lastelement = nums[l]
8        while r < len(nums):
9            if nums[r] <= lastelement:
10                l = r
11            lastelement = nums[r]
12            longest = max(longest, r - l + 1)
13            r += 1
14        return longest