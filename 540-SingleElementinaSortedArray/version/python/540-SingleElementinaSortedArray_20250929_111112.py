# Last updated: 9/29/2025, 11:11:12 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search based on the index whether it's shifted ovfer or not. we always need to check on a specific index i think it's even before doing the check
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # we always want to check mid as the even index so we can check the adj index correctly and safely
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]: # we're to the left of the single num bc order is still good
                l = mid + 2 # we need to plus one or two to account for the even ness. usualyl it would be just + 1 but bc we know that the number mid is at AND the number next o mid is the same, that means we can just skip to mid + 2 to check if that is the single number bc we cant have both r and l as mid, the cycle could never stop. so we need left to be the triggerer
            else: # nums mid is not equal to nums mid + 1
                r = mid # 2
        return nums[l]