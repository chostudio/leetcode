# Last updated: 9/11/2025, 12:30:57 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxAmount = 0
        for i in range(len(accounts)):
            currentAmount = sum(accounts[i])
            maxAmount = max(maxAmount, currentAmount)
        return maxAmount