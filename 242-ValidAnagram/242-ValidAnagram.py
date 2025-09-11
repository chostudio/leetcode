# Last updated: 9/11/2025, 12:32:09 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = defaultdict(int)
        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        for x in hashmap.values():
            if x != 0:
                return False
        return True