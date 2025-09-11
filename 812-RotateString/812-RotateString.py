# Last updated: 9/11/2025, 12:31:31 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s