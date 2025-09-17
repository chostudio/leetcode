# Last updated: 9/17/2025, 1:55:32 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        l = 0
        zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0: # it's a zero, have to do stuff
                zeros += 1
                while zeros > k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            longest = max(longest, r - l + 1) # always can check max longest on every iteration, no need to put inside of a conditional
        return longest