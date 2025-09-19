# Last updated: 9/18/2025, 8:34:06 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        temp = x
        while temp > 0:
            reverse *= 10 # only times by 10 afterwards if another number dont do it on the first attempt after adding a new number bc what if only one number
            reverse += temp % 10
            temp = temp // 10
        return reverse == x