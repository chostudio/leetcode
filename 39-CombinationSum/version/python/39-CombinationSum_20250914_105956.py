# Last updated: 9/14/2025, 10:59:56 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        def backtrack(i, amount):
            if amount == 0:
                ans.append(arr.copy())
                return
            elif amount < 0 or i >= len(candidates): # dont forget index out of bounds
                return 
            
            # keep taking at this index AND move on
            arr.append(candidates[i])
            backtrack(i, amount - candidates[i])
            arr.pop()
            backtrack(i + 1, amount) # dont minus again here

        backtrack(0, target)
        return ans