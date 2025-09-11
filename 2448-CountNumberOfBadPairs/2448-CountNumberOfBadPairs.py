# Last updated: 9/11/2025, 12:30:42 PM
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # hashmap in order to count the number of frequency of each number ( could be multiple of each which counts for more pairs )
        hashmap = defaultdict(int)
        good_pairs = 0
        # two sum intuition where u use a hashmap and use it as a past tracker. in this one i got stumped bc there were two unknowns. but you can combine them into one unknown by rearranging the equation AND preemptively combinbing them using math into the hashmap or set
        # if in set then that means it'll be smaller index
        for i in range(len(nums)):
            # count number of good pairs and then minus that from total pairs to get bad pairs?
            # first conditional is if theres others inside the set that could be bad pairs
            # rearrange i - j == nums[i] - nums[j] to get i on one side
            good_pairs += hashmap[nums[i] - i]

            hashmap[nums[i] - i] += 1
            # combinatorics for # of total pairs
        return (len(nums)*(len(nums)-1))//2 - good_pairs