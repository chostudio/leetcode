# Last updated: 9/11/2025, 12:31:53 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        se = set()
        count = 0
        for i in s:
            if i in se:
                se.remove(i)
                count += 2
            else:
                se.add(i)
        return count if len(se) == 0 else count + 1