# Last updated: 9/11/2025, 12:30:41 PM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for i in nums:
            if i % 2 == 0:
                hash[i] += 1
        num = -1
        freq = 0
        for x in hash.keys():
            if hash[x] > freq:
                freq = hash[x]
                num = x
            elif hash[x] == freq:
                num = min(x, num)
        return num
