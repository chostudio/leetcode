# Last updated: 9/11/2025, 12:32:29 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for i in nums:
            ones = (i ^ ones) & ~twos
            twos = (i ^ twos) & ~ones
        return ones