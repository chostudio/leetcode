# Last updated: 5/9/2026, 7:50:27 PM
1class Solution:
2    def concatWithReverse(self, nums: list[int]) -> list[int]:
3        # rev = reverse(nums)
4        return nums + nums[::-1]