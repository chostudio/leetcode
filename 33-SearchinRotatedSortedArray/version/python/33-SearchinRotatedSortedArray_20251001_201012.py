# Last updated: 10/1/2025, 8:10:12 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min then find target
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) //2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        smallest = l
        l, r = 0, len(nums)-1
        if nums[smallest] <= target <= nums[r]:
            l = smallest
        else:
            r = smallest
        
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] < target:
                r = mid - 1
        return -1