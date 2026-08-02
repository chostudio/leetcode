# Last updated: 8/2/2026, 9:58:17 AM
1class Solution:
2    def maximalSquare(self, matrix: List[List[str]]) -> int:
3        # if its a one along the top or left edge, then the max it can be is one. we can have a 2ddp arr that mirros the og array size and at each point we can have 1. we check the left, top, topleft diag (3 check) if all those are ones, we can say 2. if all above say 2, then we can set curr as 3, see where im going with that? then area is just the max one we encounter and say var * var == area. if any one of the left, top, topleft is 0 then the (assuming we check for 1 first) the the max of this one can only be one bc we need square, not any rectangle.
4        m, n = len(matrix), len(matrix[0])
5        dp = [[0] * n for _ in range(m)]
6
7        maxside = 0
8        for r in range(m):
9            for c in range(n):
10                if matrix[r][c] == "0":
11                    continue
12                # else 1
13                # if on edge then most 1 can be is 1
14                if r == 0 or c == 0:
15                    dp[r][c] = 1
16                    maxside = max(maxside, 1)
17                    continue # no sense checking for top left topleft bc they wont exist
18                # now gaurenteed that we are not on edge so we can check the left, top, topleft
19                prev = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) # bc if one is 0 then it cannot be a full square so we want min
20                dp[r][c] = prev + 1
21                maxside = max(maxside, dp[r][c])
22        return maxside * maxside
23