# Last updated: 9/11/2025, 12:31:54 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == len(s)