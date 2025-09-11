# Last updated: 9/11/2025, 12:30:48 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            arr.append(i)
        for j in nums:
            arr.append(j)
        return arr