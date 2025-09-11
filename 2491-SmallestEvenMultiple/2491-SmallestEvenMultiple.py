# Last updated: 9/11/2025, 12:30:40 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            return 2 * n
        return n