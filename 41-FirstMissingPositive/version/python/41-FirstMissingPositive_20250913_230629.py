# Last updated: 9/13/2025, 11:06:29 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # im solving it bc the inplace trick makes it not really a hard tbh
        # O(1) auxiliary space means no added O(n) array. BUT you can edit the input array (not recommended in production but you can do it for leetcode to 'get around') since space complexity is comprised of auxillary space (any temp vars you make)
        # first we dont care about any negatives or 0 so get rid of them and we also dont care if the number is wayyyy biggger than n
        n = len(nums) # multiple loops so making end of nums a var is easier
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n: # you need "or nums[i] > n"
                nums[i] = n + 1
        
        # negate
        for i in range(n):
            val = abs(nums[i]) # you need to abs everything bc if it is negatived from a previous number, we still need to properly get the curr number and negate another number
            # negate the index that matches the value. minus 1 bc 0 index should be 1        
            if val > 0 and val <= n: # aka have we visited it already. also to not get index out of bounds make sure that it's not outside the length of the array
                nums[val -1] = -abs(nums[val -1]) # we want the value at this index to be negative. however, if it is already negative then we want to keep it negative, not doubel negative a positive
        
        # now find the first positive number ( we didnt negate it so that index number is not there ) OR if we get through entire array then n + 1 is the smallest pos not there
        for i in range(n):
            if nums[i] > 0:
                return i + 1 # plus one bc the 0 index means we shifted back one . e.g. we need to srat at one
        return n + 1

