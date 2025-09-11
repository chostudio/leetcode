# Last updated: 9/11/2025, 12:31:58 PM
import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) //2
            new_mid = math.ceil(mid)
            double = new_mid * new_mid
            if double == num:
                return True
            elif double > num:
                right = mid - 1
            else:
                left = mid + 1
        return False