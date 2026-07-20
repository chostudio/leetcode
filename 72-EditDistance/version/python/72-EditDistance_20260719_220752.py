# Last updated: 7/19/2026, 10:07:52 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        # to remove char, just index + 1. to replace char say it matches the other one and +1 on both indicies. to insert char say we dont +1 on the one we're inserting on but then ig we would +1 on both indicies? gotta think about it for a sec but yeah
4        # okay it's word 1 to word 2
5        # minimum to reach a point
6        dp = [[-1] * len(word2) for _ in range(len(word1))]
7
8        def dfs(i, j):
9            if i >= len(word1) and j >= len(word2):
10                return 0 # we reach end
11            # what if we reach the end of one but not the end of the other one?
12            # okay so dont bother with trying to continue the dfs. if len of 1 is more than the other and we reach the end of the other then we know that num of additional operations is just however many chars are left in the longer one so just return the mathof however many is left of other word
13            if i >= len(word1):
14                return len(word2) - j # no need -1 ones here
15            if j >= len(word2):
16                # we reach end of one
17                return len(word1) - i
18            if dp[i][j] != -1:
19                return dp[i][j]
20            minimum = inf
21            # if equal we aint gotta do nothing, ideal
22            if word1[i] == word2[j]:
23                # notice here that we dont + 1 bc we dont do any operations
24                minimum = min(minimum, dfs(i + 1, j + 1))
25
26            # else we gotta do something, either replace or remove the curr char of word 1
27            
28            # else bc if it is the same then we wouldnt do a operation
29            else:
30                # to delete a char is i + 1 (skkip over the curr char of word1)
31                minimum = min(minimum, dfs(i + 1, j) + 1)
32                # to insert a char is to match it with word2 but then when we incremenet it to next word1 it's the same char as b4 o no need move word1 essentially but move other pointer ahhhhh
33                minimum = min(minimum, dfs(i, j + 1) + 1)
34                # replace a char is both increment
35                minimum = min(minimum, dfs(i + 1, j + 1) + 1)
36
37            dp[i][j] = minimum
38            return minimum
39        
40       
41        return dfs(0,0)