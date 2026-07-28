# Last updated: 7/27/2026, 8:38:40 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        # if they are not equal thtne we can move in one of the things, if both are equal then move both inward and add
4
5        # top down move in
6        # l, r have we visited this exact double position before, if so whats the amount we found
7        n = len(s)
8        # cannot be 0 bc 0 is a legit value we could have, we need a "hey this changed or did not value"
9        dp = [[inf] * n for i in range(n)]
10        
11        # dp function where we populate back up the chain via returning integers
12        # remember that the 
13        def dfs(l, r):
14            if l > r or r < 0 or l >= n:
15                return 0 # crossed each other or OOB
16            
17            # if we visited alr
18            if dp[l][r] != inf: # aka changed
19                return dp[l][r]
20            maxatthispoint = 0
21            if s[r] == s[l]:
22                if l != r:
23                    maxatthispoint = max(maxatthispoint, dfs(l+1, r-1)) + 2
24                else: # literally on the same index mid point
25                    return 1
26            
27            else:
28                maxatthispoint = max(maxatthispoint, dfs(l, r -1))
29                maxatthispoint = max(maxatthispoint, dfs(l+1, r))
30            # maxatthispoint = max(maxatthispoint, ifright, ifleft)
31            dp[l][r] = maxatthispoint
32            return maxatthispoint # remember to return the dfs up the chain here. assign and return
33        return dfs(0, n-1)
34            
35
36            
37