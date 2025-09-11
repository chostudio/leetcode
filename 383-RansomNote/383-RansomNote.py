# Last updated: 9/11/2025, 12:31:58 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = defaultdict(int)
        for i in magazine:
            hash[i] += 1
        for x in ransomNote:
            if hash[x] <= 0:
                return False
            hash[x] -= 1
        return True