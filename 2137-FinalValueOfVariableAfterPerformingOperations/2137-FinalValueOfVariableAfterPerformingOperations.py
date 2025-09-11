# Last updated: 9/11/2025, 12:30:47 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in operations:
            if i == "++X" or i == "X++":
                count += 1
            elif i == "--X" or i == "X--":
                count -= 1
        return count