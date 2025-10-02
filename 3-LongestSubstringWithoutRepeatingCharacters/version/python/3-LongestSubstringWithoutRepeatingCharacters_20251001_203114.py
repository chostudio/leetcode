# Last updated: 10/1/2025, 8:31:14 PM
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = defaultdict(int)
        for r in range(len(s)):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            longest = max(longest, r - l + 1)
            seen[s[r]] = r
        return longest