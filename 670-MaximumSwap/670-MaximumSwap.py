# Last updated: 9/11/2025, 12:31:38 PM
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        max_digit = "0" # has to be 0 not nums[0]
        max_index = -1
        swap_i = -1
        swap_j = -1
        for i in reversed(range(len(nums))):
            if nums[i] > max_digit:
                max_digit = nums[i]
                max_index = i
                # swappable
            if nums[i]< max_digit:
                swap_i = i
                swap_j = max_index
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]
        return int("".join(nums))