# Last updated: 7/19/2026, 3:54:24 PM
1class Solution:
2    def combinationSum4(self, nums: List[int], target: int) -> int:
3        # can reframe the problem to think of it like top down climbing staircases where its like at each point we decrease the thing and then when we hit base case its +1 and if we hit same number case the we need to remember it like how many ways we can make this sum. 
4        # index == value. value at index = total ways we can make this number
5        seenamounts = [-inf] * (target + 1)
6
7        def dfs(curramount):
8            if curramount == 0:
9                return 1
10            if curramount < 0:
11                return 0
12            
13            # else there must be a value
14
15            # have we visited this exact amount before
16            if seenamounts[curramount] != -inf:
17                return seenamounts[curramount]
18
19            ways2make = 0
20            for num in nums:
21                ways2make += dfs(curramount - num)
22            
23            # reach the end of a path
24            seenamounts[curramount] = ways2make
25            return ways2make
26        return dfs(target)