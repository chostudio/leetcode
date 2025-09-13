# Last updated: 9/13/2025, 10:32:39 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three pointer
        start, end = -1, len(nums)
        i = 0
        while i < end: # needs to be the end pointer bc everyhitng behind it is just twos and we dont really want to swap any of them since they're in the correct place already so just end it "early"
            if nums[i] == 0:
                start += 1
                # swap
                nums[start], nums[i] = nums[i], nums[start]
                # the reason we do this because when we swap we actually dont know what the value is and we need to check it again but for loop increments every time so minusing by one keeps it at the same index. could also use a while loop instead
                # WE DONT do i -= 1 HERE but we do it in the other one why?
            elif nums[i] == 2:
                end -= 1
                # swap
                nums[end], nums[i] = nums[i], nums[end]
                i -= 1
            i += 1