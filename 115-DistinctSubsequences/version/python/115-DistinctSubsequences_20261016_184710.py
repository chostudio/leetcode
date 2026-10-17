# Last updated: 10/16/2026, 6:47:10 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        
4        if len(t) > len(s): return 0 # too long
5
6        memo = defaultdict(int) # num of ways from this pos
7        def dfs(i, j):
8            if i >= len(s) and j >= len(t):
9                return 1
10            if j >= len(t): # success if t reach end
11                return 1
12            if i >= len(s): # not success if i reach end but j didn't though
13                return 0 # one reach end but other didn't, therefore not equal
14
15            if (i, j) in memo: # have we been to this exact point b4
16                return memo[(i, j)]
17            
18            # otherwise we havent been here
19
20            # actually even if not equal, we always wna tot (i, 0) is possible. if not equal
21            amount = 0
22            
23            if s[i] == t[j]:
24                amount += dfs(i +1, j + 1)
25                # amount += dfs(i, j + 1) never move j alone
26            amount += dfs(i + 1, j)
27            # if not equal, then chance when moving 
28            # amount += dfs(i + 1, 0)
29            
30            # letters are equal to each other now
31
32            # we can take both letters by + 1, skip one or other letter
33            
34            # i dont think theres option where we don't move otherwise infinite
35
36            # save amount in memo then reutrn back up chain
37            memo[(i, j)] = amount
38            return amount            
39
40        return dfs(0, 0)