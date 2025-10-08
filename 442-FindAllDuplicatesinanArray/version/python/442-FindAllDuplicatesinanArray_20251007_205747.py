# Last updated: 10/7/2025, 8:57:47 PM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # negative index hack ughhhh
        res = []
        # the reason we use abs (bc it might be negative)
        # the reason why we do i-1 is that if the number is of value == n (len of array) then the index wouldn't exist
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            nums[abs(i)-1] = -nums[abs(i)-1]
        return res