# Last updated: 2/28/2026, 6:33:11 PM
1class Solution:
2    def trimTrailingVowels(self, s: str) -> str:
3        if len(s) == 0:
4            return ""
5        i = len(s) - 1
6        vowels = ['a', 'e', 'i', 'o', 'u']
7        while i >= 0 and s[i] in vowels:
8            i -= 1
9        return s[:i+1]