# Last updated: 9/11/2025, 12:30:59 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hashmap = defaultdict(int)
        for n in nums:
            if n in hashmap:
                count += hashmap[n] # the count of past numbers like it to make a pair
            hashmap[n] += 1
        return count