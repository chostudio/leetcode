# Last updated: 9/11/2025, 12:32:21 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        # while n exists aka not 0
        while n:
            sum += n % 2
            # this shifts n to the right by 1 bit
            n = n >> 1
        return sum