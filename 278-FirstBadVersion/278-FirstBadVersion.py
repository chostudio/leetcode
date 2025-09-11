# Last updated: 9/11/2025, 12:32:07 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = l + (r - l) // 2 # writing the midpoint like this avoids overflow
            if isBadVersion(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        return l