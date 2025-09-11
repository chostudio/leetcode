# Last updated: 9/11/2025, 12:32:31 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            leftLetter = s[l].lower()
            rightLetter = s[r].lower()
            if leftLetter.isalnum() and rightLetter.isalnum():
                if leftLetter == rightLetter:
                    l += 1
                    r -= 1
                else:
                    return False
            l += (not leftLetter.isalnum())
            r -= (not rightLetter.isalnum())
        return True