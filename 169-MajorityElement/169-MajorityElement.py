# Last updated: 9/11/2025, 12:32:23 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        answer = 0
        maxVar = 0
        for x in hashmap.keys():
            if hashmap[x] > maxVar:
                maxVar = hashmap[x]
                answer = x
        return answer
