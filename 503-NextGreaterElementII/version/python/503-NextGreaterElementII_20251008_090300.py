# Last updated: 10/8/2025, 9:03:00 AM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # im thinking two loops. first one is normal loop with queu add then break then second one just loops through again
        # (value, index)
        stack = []
        ans = [-1] * len(nums)
        i = 0
        while i < len(nums):
            while len(stack) != 0 and stack[-1][0] < nums[i]:
                val, index = stack.pop()
                ans[index]= nums[i]
            stack.append((nums[i], i))
            i += 1
        
        i = 0
        # go again but dont readd anything
        while i < len(nums):
            while len(stack) != 0 and stack[-1][0] < nums[i]:
                val, index = stack.pop()
                ans[index]= nums[i]
            i += 1
        return ans