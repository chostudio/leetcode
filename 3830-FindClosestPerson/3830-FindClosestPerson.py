# Last updated: 9/11/2025, 12:30:18 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) > abs(y-z):
            return 2
        if abs(x-z) < abs(y-z):
            return 1
        else:
            return 0