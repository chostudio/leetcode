# Last updated: 11/1/2025, 12:04:21 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # dont count the pivot index number (aka just sum it up afterwards)
        index = -1
        total = sum(nums)
        running = 0
        for i in range(len(nums)):
            if running == total - running - nums[i]: # we dont count "i" the current index we're at as part of the total. strictly left anf right of it
                index = i
                break # leftmost index so break early
            running += nums[i]
        return index