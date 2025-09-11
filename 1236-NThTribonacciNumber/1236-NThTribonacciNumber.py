# Last updated: 9/11/2025, 12:31:15 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0,0,1
        for i in range(n):
            temp = first + second + third
            first = second
            second = third
            third = temp
        return second