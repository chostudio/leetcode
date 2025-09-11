# Last updated: 9/11/2025, 12:31:04 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(0, n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
