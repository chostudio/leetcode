# Last updated: 9/11/2025, 12:30:27 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0
        totalFreq = 0
        hashmap = defaultdict(int)
        # hash everything in dictionary and get max freq
        for i in nums:
            hashmap[i] += 1
            if hashmap[i] > maxFreq:
                maxFreq = hashmap[i]

        # check to see how many values are equal to the max freq
        for value in hashmap.values():
            if value > maxFreq:
                totalFreq = value
            elif value == maxFreq:
                totalFreq += value
        return totalFreq