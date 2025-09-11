# Last updated: 9/11/2025, 12:32:30 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor