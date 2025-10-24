# Last updated: 10/23/2025, 7:46:36 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if not same then we can  check if r == l + 1 or if l = r - 1 if either of those combos work then yes we can and weflip a boolean and cotinue else false else else boolean already flipped false
        # so we cant just randomly choose a left or right if it matches bc we dont know if the rest of the string will be fine so the trick is to have a helper function that is triggered if there is a mismatch that checks the rest (using both index swaps) and if at least one of them is a valid palindrome then return true or false immediately
        def isrestpalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return isrestpalindrome(l+1, r) or isrestpalindrome(l, r-1)
            l += 1
            r -= 1
        return True