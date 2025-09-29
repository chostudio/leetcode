# Last updated: 9/29/2025, 10:41:36 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            j = 0
            while i + j < len(haystack) and j < len(needle) and haystack[i+j] == needle[j]:
                j += 1
            if j == len(needle):
                return i
        return -1