# Last updated: 9/14/2025, 10:50:44 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = [] # outside so we can mutate it
        def backtrack(i):
            if i == len(nums):# base case we reach the end
                ans.append(arr.copy())
                return # need this
            
            arr.append(nums[i])
            backtrack(i + 1)
            arr.pop()
            backtrack(i + 1)
        backtrack(0)
        return ans