# Last updated: 9/11/2025, 12:30:31 PM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        arr = sorted(nums)
        l, r = 0, len(nums)-1
        count = 0
        while l < r:
            if arr[l] + arr[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count