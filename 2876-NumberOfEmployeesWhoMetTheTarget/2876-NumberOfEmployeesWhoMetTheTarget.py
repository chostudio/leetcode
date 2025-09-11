# Last updated: 9/11/2025, 12:30:33 PM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count