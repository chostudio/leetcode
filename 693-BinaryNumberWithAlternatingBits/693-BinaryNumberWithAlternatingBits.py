# Last updated: 9/11/2025, 12:31:36 PM
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string = str(bin(n)[2:])
        if n <= 2:
            return True
        l, r = 0, 1
        while r < len(string):
            if string[l] == string[r]:
                return False
            r += 1
            l += 1
        return True