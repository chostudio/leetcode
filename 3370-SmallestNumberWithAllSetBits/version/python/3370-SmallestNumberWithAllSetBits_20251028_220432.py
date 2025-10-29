# Last updated: 10/28/2025, 10:04:32 PM
class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 0
        while True:
            zeros = 0
            for c in bin(i + n)[2:]: # python bin is "0b1101010110"
                if c == "0":
                    zeros += 1
                    break
            if zeros == 0:
                return i + n
            i += 1