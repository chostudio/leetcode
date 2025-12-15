# Last updated: 12/14/2025, 4:57:35 PM
1from collections import defaultdict
2class Solution:
3    def lengthOfLongestSubstring(self, s: str) -> int:
4        longest = 0
5        l = 0
6        seen = defaultdict(int)
7        for r in range(len(s)):
8            if s[r] in seen and l <= seen[s[r]]:
9                l = seen[s[r]] + 1
10            longest = max(longest, r - l + 1)
11            seen[s[r]] = r
12        return longest