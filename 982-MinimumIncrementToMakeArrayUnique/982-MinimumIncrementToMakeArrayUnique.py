# Last updated: 9/11/2025, 12:31:24 PM
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # sort, then adj pointer, incredmenting until curr is greater than last one. nlogn time
        if len(nums) == 1:
            return 0
        # guanrentee its at least two index
        nums.sort()
        print(nums)
        moves = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                # needs to be greater than prev + 1
                moves += nums[i - 1] - nums[i] + 1
                # then you need to actually update it
                nums[i] = nums[i - 1] + 1
        return moves
