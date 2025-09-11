# Last updated: 9/11/2025, 12:30:23 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum