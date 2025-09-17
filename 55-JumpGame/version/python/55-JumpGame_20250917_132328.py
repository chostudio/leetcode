# Last updated: 9/17/2025, 1:23:28 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # always take the bigger value and always minus one (bc that's a jump) on every iteration
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr == 0:
                return False
            curr -= 1
            curr = max(curr, nums[i])
            
        return True