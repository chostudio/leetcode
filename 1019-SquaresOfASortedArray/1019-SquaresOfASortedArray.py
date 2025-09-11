# Last updated: 9/11/2025, 12:31:21 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        n = len(nums)-1
        newNums = [0]*len(nums)
        
        while n >=0:
            one = pow(nums[left], 2)
            two = pow(nums[right], 2)
            
            if one > two:
                newNums[n] = one
                left += 1
            else:
                newNums[n] = two
                right -= 1
            n -=1
        return newNums
                
        