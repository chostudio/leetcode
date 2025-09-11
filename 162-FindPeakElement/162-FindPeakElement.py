# Last updated: 9/11/2025, 12:32:24 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) //2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
