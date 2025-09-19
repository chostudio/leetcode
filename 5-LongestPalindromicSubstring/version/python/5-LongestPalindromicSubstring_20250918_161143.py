# Last updated: 9/18/2025, 4:11:43 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # required base case
        if len(s) <= 1:
            return s
        longest = ""

        # babad
        def palindrome(indexA, indexB):
            # word = ""
            i = 0
            while indexA-i >= 0 and indexB+i <= len(s) - 1 and s[indexA-i] == s[indexB+i]:
                i += 1

            return s[indexA-i+1:indexB+i] # python splice syntax  requires a plus one on the left side bc it's inclusive??? i guess since it's like [1:] everything after one

        for index in range(len(s)-1):
            pal = palindrome(index, index)
            val = palindrome(index, index+1)

            pal = val if len(val) > len(pal) else pal
            if len(pal) > len(longest):
                longest = pal
        return longest