# Last updated: 10/23/2025, 9:48:11 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
            l, r = 0, len(s) - 1
            while l <= r:
                left = s[l].lower() 
                right = s[r].lower() 
                if left.isalnum() and right.isalnum():
                    
                    if right != left:
                        return False
                    l += 1
                    r -= 1
                else: # one or both is not alpha numeric char
                    if not left.isalnum():
                        l += 1
                    if not right.isalnum():
                        r -= 1
            return True