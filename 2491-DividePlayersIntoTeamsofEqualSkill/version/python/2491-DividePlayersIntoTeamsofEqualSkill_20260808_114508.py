# Last updated: 8/8/2026, 11:45:08 AM
1class Solution:
2    def dividePlayers(self, weight: List[int]) -> int:
3        l, r = 0, len(weight)-1
4        weight.sort()
5        
6        ans = 0
7        samesum = inf
8        while l < r:
9            left, right = weight[l], weight[r]
10            if samesum == inf: # first go around
11                samesum = left + right
12            else:
13                if samesum != left + right:
14                    return -1 # not the same pair
15            ans += left * right
16            l += 1
17            r -= 1
18
19        return ans
20