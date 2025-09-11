# Last updated: 9/11/2025, 12:30:19 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # yo it's not sorted so hashmap. if duplicate then remember furthest one
        furthestDup = 0
        hashmap = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hashmap:
                # have to max bc there's a possibility that another duplicate number may have it's second instance further on but its first instance much earlier than another one
                furthestDup = max(furthestDup, hashmap[nums[i]])
            hashmap[nums[i]] = i + 1
        # there's probably an easier mathmatical way of calculating how many chops of length three you need using division but this works
        amount = 0
        while furthestDup > 0:
            amount += 1
            furthestDup -= 3
        return amount