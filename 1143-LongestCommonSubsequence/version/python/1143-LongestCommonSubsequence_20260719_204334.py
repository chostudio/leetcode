# Last updated: 7/19/2026, 8:43:34 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        #does it matter which word is longer? sure
4        dp = [[-1] * len(text2) for _ in range(len(text1))]
5
6        # longest = 0
7
8        # pick (if same) or skip (dont choose to use a letter it and move on) a letter basically e.g. abc and bca 0, 0 -> 0,1 is same. we move one index forward while other stay stagnant, we move other index while other stays, or if both same then move both. (there woultnd be a acase where if same and we wouldnt take both tbh) okay we got the recursion lets boogie and top down it
9
10        def dfs(t1, t2):
11            if t1 == len(text1):
12                return 0
13            if t2 == len(text2):
14                return 0
15            
16            if dp[t1][t2] != -1:
17                return dp[t1][t2]
18            
19            sofar = max(dfs(t1+1, t2), dfs(t1, t2+1))
20            # if match then add letter to sequence
21            if text1[t1] == text2[t2]:
22                sofar = max(sofar, dfs(t1+1, t2+1) +1)# put the + 1 inside the dfs chain not outside
23            dp[t1][t2] = sofar
24            # nonlocal longest
25            # longest = max(longest, sofar)
26            return sofar
27
28        # apparently you dont need to init a longest nonlocal var and the algo handles it populating up alr
29        return dfs(0,0) # you could pass in param "matches" that +1 increments or return it populate it bubble it up the recufrsion chain
30
31        # return longest