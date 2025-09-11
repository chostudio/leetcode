# Last updated: 9/11/2025, 12:30:30 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2