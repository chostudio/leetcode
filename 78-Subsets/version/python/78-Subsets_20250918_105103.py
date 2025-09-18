# Last updated: 9/18/2025, 10:51:03 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]
        ans = []
        temp = [] # 1, 2, 3 | 1, 2 | 1 | [] |
        # 
        def backtrack(i): # 3
            if i >= len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            backtrack(i +1)
            temp.pop()
            backtrack(i + 1)

        backtrack(0)
        return ans