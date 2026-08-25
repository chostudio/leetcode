# Last updated: 8/24/2026, 9:57:14 PM
1class Solution:
2    def numSquares(self, n: int) -> int:
3        
4        # 1d dp like coin change. to make the "coins" we can use, generate the arr of perfect squares we can use from 1 -> n
5
6        i = 1
7        dp = defaultdict(int)
8
9        squares = []
10        while i * i <= n:
11            squares.append(i * i)
12            dp[i * i] = 1 # there is 1 way to make an ideal square in the best way
13            i += 1
14        
15        # at this num : smallest amount of perfect squares to get it
16        def dfs(val):
17            if val == 0:
18                return 0
19            if val == 1:
20                return 1
21            if val in dp:
22                return dp[val]
23            
24            smallestatthisnum = n
25            for num in squares:
26                # there are a lot of invalid ones if we go past 0 that we shouldnt count
27                if val - num >= 0:
28                    smallestatthisnum = min(smallestatthisnum, dfs(val - num) + 1)
29            
30            dp[val] = smallestatthisnum
31            return smallestatthisnum
32        return dfs(n)