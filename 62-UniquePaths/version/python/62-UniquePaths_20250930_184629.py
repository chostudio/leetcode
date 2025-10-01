# Last updated: 9/30/2025, 6:46:29 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # i would argue the hard part anout dp is knowing the when to do it and how to in the scenario. the actual code logic is not tooo bad 
        # u can only go down or right. we start from bottom right and iterate upwards left and calc with another premade 2d matrix with values
        dp = [[0] * n for i in range(m)]

        # inclusive, exclusive
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r < m-1 and c < n-1:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
                else:
                    dp[r][c] = 1 # if at bottom or right edges (only one path)
        return dp[0][0]