# Last updated: 7/30/2026, 7:39:58 AM
1class Solution:
2    def subArrayRanges(self, nums: List[int]) -> int:
3        # im like 90% you could prefix sum from both directions the biggest weve seen so far at this index but also lik we wont comparing biggest everytime itll be the nxt door neighbor too
4
5        # okauy brtue force is double for looop. how to effficent
6        ans = 0
7        for i in range(len(nums)):
8            biggest, smallest = nums[i], nums[i]
9            for j in range(i+1, len(nums)):
10                biggest = max(biggest, nums[j])
11                smallest = min(smallest, nums[j])
12                ans += biggest - smallest
13        return ans