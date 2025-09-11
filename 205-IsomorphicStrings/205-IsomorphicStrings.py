# Last updated: 9/11/2025, 12:32:19 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            if ((s[i] in hashS and hashS[s[i]] != t[i]) or (t[i] in hashT and hashT[t[i]] != s[i])):
                return False
            hashS[s[i]] = t[i]
            hashT[t[i]] = s[i]
        return True