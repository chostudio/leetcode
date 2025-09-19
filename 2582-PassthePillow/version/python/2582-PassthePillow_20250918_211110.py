# Last updated: 9/18/2025, 9:11:10 PM
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 1
        direction = 1
        while time:
            index += direction
            if index == n:
                direction = -1
            if index == 1:
                direction = 1
            time -= 1
        return index