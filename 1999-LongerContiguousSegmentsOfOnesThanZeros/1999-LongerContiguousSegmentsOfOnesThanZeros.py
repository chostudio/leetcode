# Last updated: 9/11/2025, 12:30:50 PM
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = 0
        maxones = 0
        zeros = 0
        maxzeros = 0
        for i in range(len(s)):
            if s[i] == "1":
                zeros = 0
                ones += 1
                maxones = max(ones, maxones)
            else:
                ones = 0
                zeros += 1
                maxzeros = max(maxzeros, zeros)
        return maxones > maxzeros