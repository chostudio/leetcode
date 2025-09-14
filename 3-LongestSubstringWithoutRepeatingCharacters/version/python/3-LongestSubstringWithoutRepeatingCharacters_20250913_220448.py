# Last updated: 9/13/2025, 10:04:48 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        letters = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in letters:
                while s[r] in letters:
                    letters.remove(s[l])
                    l += 1
            letters.add(s[r])
            r += 1
            current = r - l
            longest = max(current, longest)
        
        return longest