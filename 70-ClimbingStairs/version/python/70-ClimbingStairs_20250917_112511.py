# Last updated: 9/17/2025, 11:25:11 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, prevprev = 2, 1
        ans = 0
        for i in range(3, n+1):
            temp = ans
            ans = prev + prevprev
            prevprev = prev
            prev = ans
        return ans
