# Last updated: 9/19/2025, 8:52:01 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxprofit = 0
        while r < len(prices):
            maxprofit = max(maxprofit, prices[r]- prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxprofit