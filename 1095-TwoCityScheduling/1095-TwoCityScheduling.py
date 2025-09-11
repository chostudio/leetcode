# Last updated: 9/11/2025, 12:31:19 PM
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # instead of brute forcing, send everyone to A, then send the people with the biggest difference to B, and refund from A. this makes our job easier since we have a starting point to compare?
        minCost = 0
        posRefunds = []
        for cost in costs:
            a, b = cost[0], cost[1]
            minCost += a
            # minusing and plussing a is like precalc nothing happened IF we choose the difference in the posRefunds
            posRefunds.append(b-a)
        posRefunds.sort() # if the cost of a was much bigger than b, then we choose the first half. the values in it can be negative. 
        for i in range(len(posRefunds) // 2):
            minCost += posRefunds[i]
        return minCost