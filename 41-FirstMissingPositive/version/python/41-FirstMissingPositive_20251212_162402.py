# Last updated: 12/12/2025, 4:24:02 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        # im solving it bc the inplace trick makes it not really a hard tbh
4        # O(1) auxiliary space means no added O(n) array. BUT you can edit the input array (not recommended in production but you can do it for leetcode to 'get around') since space complexity is comprised of auxillary space (any temp vars you make)
5        # first we dont care about any negatives or 0 so get rid of them and we also dont care if the number is wayyyy biggger than n
6        n = len(nums) # multiple loops so making end of nums a var is easier
7        for i in range(n):
8            if nums[i] <= 0:
9                nums[i] = n + 1
10        
11        # negate
12        for i in range(n):
13            val = abs(nums[i]) # you need to abs everything bc if it is negatived from a previous number, we still need to properly get the curr number and negate another number
14            # negate the index that matches the value. minus 1 bc 0 index should be 1        
15            if val > 0 and val <= n: # aka have we visited it already. also to not get index out of bounds make sure that it's not outside the length of the array
16                nums[val -1] = -abs(nums[val -1]) # we want the value at this index to be negative. however, if it is already negative then we want to keep it negative, not double negative and positive it. you must have the abs here as well
17        
18        # now find the first positive number ( we didnt negate it so that index number is not there ) OR if we get through entire array then n + 1 is the smallest pos not there
19        for i in range(n):
20            if nums[i] > 0:
21                return i + 1 # plus one bc the 0 index means we shifted back one . e.g. we need to srat at one
22        return n + 1
23
24