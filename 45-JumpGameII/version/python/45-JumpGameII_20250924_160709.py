# Last updated: 9/24/2025, 4:07:09 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        # we want furthest. this is determined by the value of the current element as well as its index
        # instead of naming the variable "i", bc it's a range so near-far makes more sense
        jumps = 0
        furthest = 0
        near = 0
        # interesting, its while furthest is not at the end yet NOT i/near, which makes sense
        while furthest < len(nums)-1: # no equality operator bc once we reach final elem dont retrigger it
            new_furthest = 0 # we need to reset furthest every time and not max it everytime bc what if the prev max was greater than anything in our current range, wouldn't be correct so need to overwrite it
            for index in range(near, furthest+1): # start is index and end at elem range. 2nd val is exclusive so need to + 1
                new_furthest = max(new_furthest, index + nums[index]) # index+ val of elem        
            near = furthest # update new range to be the end of the prev range? I would think it to be where the new index was but i guess this makes sense because whatever index we pick, we know that that one was the furthest reaching one and there's no need to double check the prevmax->new_range range since it'll always be lesser
            furthest = new_furthest
            jumps += 1
        return jumps