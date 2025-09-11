# Last updated: 9/11/2025, 12:32:02 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            # find l, r, then swap
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        return "".join(s)