# Last updated: 9/11/2025, 12:31:22 PM
class Solution:
    def fib(self, n: int) -> int:
        first, second = 0, 1
        for i in range(n):
            temp = second + first
            first = second
            second = temp
        return first