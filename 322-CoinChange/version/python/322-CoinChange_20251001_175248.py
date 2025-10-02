# Last updated: 10/1/2025, 5:52:48 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # watch me dp ts
        # u set up the 1d dp array wrong syntax wise
        dp = [inf] * (amount + 1) # +1 bc 0th index
        dp[0] = 0 # base case why so that if a coin == i another coin wouldn't be added it would just be 1

        # start at 1 bc no coin can be 0
        for i in range(1, amount+1): # inclusive exclusive remember
            for coin in coins:
                if i - coin >= 0: # does prev index exist
                    dp[i] = min(dp[i], dp[i-coin] + 1) # smallesr amount of coin is prev index amount + 1 coin or where we're atm curr index (could be infinity out of range)
        return dp[amount] if dp[amount] != inf else -1