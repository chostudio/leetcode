# Last updated: 9/11/2025, 12:30:38 PM
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        regular = 0
        digit = 0
        for i in nums:
            regular += i
            temp = i
            while temp > 0:
                pop = temp % 10 # get the last number
                digit += pop
                temp //= 10 # actually remove the last number. needs ot be double slash bc that's integer division
        return abs(regular - digit)