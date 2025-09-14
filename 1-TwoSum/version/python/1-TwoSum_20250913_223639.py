# Last updated: 9/13/2025, 10:36:39 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = collections.defaultdict(int) # store index of past vals
        for i in range(len(nums)):
            difference = target - nums[i] # do the math, subtract from both sides, work backwards to get the other unknown number
            if difference in hashmap:
                return [hashmap[difference], i]
            # else
            hashmap[nums[i]] = i
        # nothing