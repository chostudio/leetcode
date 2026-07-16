# Last updated: 7/15/2026, 11:45:37 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        target = sum(nums)
4        if target % 2  != 0: return False
5
6        visited = [[inf] * (target//2 + 1) for _ in nums]
7
8        def dfs(index, currsum): # we pass in target as halfwaypoint. if any combo hits it then that means the other half must also be half and we return true
9            if currsum < 0:
10                return False
11            if currsum == 0:
12                return True
13            if index >= len(nums):
14                return False
15            # at this index, have we seen this exact sum / can we get to true from here or is it all false
16            if visited[index][currsum] != inf:
17                return visited[index][currsum] # either T or F
18            # combo sum, one we take the num, one we dont take the num.
19            # we store in in var so that we can update dp table, then return
20            result = dfs(index + 1, currsum-nums[index]) or dfs(index + 1, currsum) # take and no take options
21            visited[index][currsum] = result
22            return result
23    
24        return dfs(0, target//2)