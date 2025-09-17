# Last updated: 9/17/2025, 1:47:41 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        longest, l = 0, 0
        index = defaultdict(int)

        for r in range(len(s)):
            if s[r] in index and l <= index[s[r]]: # less than!!! think logic AND equal too
                l = index[s[r]] + 1
            else:
                longest = max(longest, r - l + 1)
            index[s[r]] = r
        return longest