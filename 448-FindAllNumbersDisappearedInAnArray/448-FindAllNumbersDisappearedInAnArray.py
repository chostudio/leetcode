# Last updated: 9/11/2025, 12:31:48 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        for i in range(1, len(nums)+1):
            s.add(i)
        for i in nums:
            if i in s:
                s.remove(i)
        return list(s)