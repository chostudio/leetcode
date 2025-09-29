# Last updated: 9/28/2025, 9:18:12 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # guarenteed that at least 3 elements makes this way easier
        l, r = 0, len(arr)-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                l = mid + 1
            else:
                r = mid
