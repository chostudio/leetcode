# Last updated: 9/25/2025, 3:16:49 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # the naive way to do this (and the way i like doing it) is checking the adj values next to the mid/peak and worrying about the index is in a valid range. but the smarter way to approach this problem is checking only two indeicies: the peak element and the value right next to it to the right. we can always guarentee that the index of the adj right pointer to the peak wont go out of bounds because we can start the right pointer at len(nums) - 1. then we return l at the end bc the l pointer would only increase by one so technically l and r should be at the same index at the end???
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid + 1] < nums[mid]: # peak must be towards leftward side likely
                r = mid
            else:
                l = mid + 1 # +1 bc it handles the what if equal case too
        return r