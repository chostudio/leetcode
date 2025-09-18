# Last updated: 9/18/2025, 1:43:17 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # "sadbutsad"
        for i in range(len(haystack)):
            j = 0
            while i + j < len(haystack) and haystack[i+j] == needle[j]:
                j += 1
                if j == len(needle):
                    return i
        return -1