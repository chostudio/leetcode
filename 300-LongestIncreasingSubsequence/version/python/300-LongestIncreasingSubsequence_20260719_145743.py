# Last updated: 7/19/2026, 2:57:43 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        # take and no take. if we get to exact point, then we want to check visited to see what the biggest one here was or like work our way up hey is it possible to get here and if so then take the bigger (kinda like greedy) amount. however the backtracking way is inefficient. the better way is to O(n^2) from this number, get the biggest from past numbers that the curr number is bigger than. there is a more efficeint (greedy) way that just says hey choose numbers bigger than this one but it's lowk cooked explaining it
4
5        best = [1] * len(nums)
6        longest = 1
7        for i in range(len(nums)):
8            bestrn = 1
9            for j in range(i):
10                # j is 0 -> i
11                if nums[i] > nums[j]:
12                    # +1 bc it's like adding the curr number to the chain
13                    bestrn = max(bestrn, best[j] + 1)
14            best[i] = bestrn
15            longest = max(longest, best[i])
16        return longest
17