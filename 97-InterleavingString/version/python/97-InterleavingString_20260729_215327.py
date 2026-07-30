# Last updated: 7/29/2026, 9:53:27 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        if len(s1) + len(s2) != len(s3):
4            return False
5        
6        dp = [[inf] * (len(s2)+1) for _ in range(len(s1)+1)]
7
8        # we technically dont need a third pointer to rep what s3 is bc we can add i + j together to get an index bc we assume taht if they move then obc s3 has to move too.
9        def dfs(i, j):
10            # has to reach the end of both. if lenegth of end 1 but not other then we keep going. # oh you know what, we can check if either the s1 or s2 letter is eqautl to the letter at s3 then if we hit end of s3 word, then true, in all other cases then is false. we should check along the way insted of genreating combo then comparing strings
11            # if we reach the end
12            if i >= len(s1) and j >= len(s2) and i + j == len(s3):
13                return True
14
15            # what if one is super out of bounds (like past a all letters) and the other one isn't done yet.
16            # then we need to do the edit distance trick and whichever word we still have left just check the end of the word and compare to rest of s3 
17            # dont need to dp cache in here? bc this is the end? ya bc out of bounds
18            if i >= len(s1):
19                return s2[j:] == s3[i+j:]
20                # dp[i][j] = result
21                # return result
22            if j >= len(s2):
23                return s1[i:] == s3[i+j:]
24                # dp[i][j] = result
25                # return result
26
27            # u forgot visited check lol
28            if dp[i][j] != inf:
29                return dp[i][j]
30            # if neither equals the curr char then obv this is cooked quit it
31            # check if in bounds first
32            s3char = s3[i+j]
33            if s1[i] != s3char and s2[j] != s3char:
34                return False
35
36            # if both letters are the same then we could realistically try either one. if only one are the same, then obv dont try either one. 
37            # if s1[i] == s3char and s2[j] == s3char:
38            #     result = dfs()
39            #     # remember to store it for future
40            #     dp[i][j] = result
41            #     return result
42            
43            # if only one, then just do the one. i dont think we can pick and skip in this one bc we need to use all letters
44            # wait if they are the same then this is fine both work
45            result = False
46            if s1[i] == s3char:
47                result = result or dfs(i + 1, j)
48            if s2[j] == s3char:
49                result = result or dfs(i, j+1)
50            # remember to store it for future
51            dp[i][j] = result
52            
53            return result
54        
55        return dfs(0,0)