# Last updated: 9/11/2025, 12:30:16 PM
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # set up two initial prefix sum arrays
        n = len(prices)
        buyEvery = [0] * (n + 1)
        ogProfit = [0] * (n+1)
        # put in values by summing it up
        for i in range(len(prices)):
            # curr is i + 1, prev is i, update curr with PAST Values only
            buyEvery[i+1] = buyEvery[i] + prices[i]
            ogProfit[i+1] = ogProfit[i] + prices[i] * strategy[i]
        
        # now set up sliding window of size k
        half = k // 2 # k is even dont worry
        l, r = 0, k
        maxSum = ogProfit[n] # the end of the prefix sum array reps the ogprofit baseline cost (aka if we didn't do anything) that we compare future to
        # r <= n also works
        while r < len(prices)+1:
            # up to left reg + | nothing half + half to all positives to SW end | + to end reg
            # forgot mid. need to be between l and r
            mid = l + half
            # real
            beforeWindow = ogProfit[l]
            afterWindow = ogProfit[n] - ogProfit[r]
            # idealized 1111
            rightHalfWindow = buyEvery[r] - buyEvery[mid]
            currSum = beforeWindow + rightHalfWindow + afterWindow
            maxSum = max(maxSum, currSum)
            l += 1
            r += 1
        
        return max(maxSum, ogProfit[n])