# Last updated: 9/11/2025, 12:32:01 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count amount of each char
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        
        # put in freq list array
        freq = [[] for i in range(len(nums)+ 1)]
        for key, val in hashmap.items():
            freq[val].append(key)

        ans = []
        for i in range(len(freq)-1, 0, -1):
            inner = 0
            while inner < len(freq[i]):
                ans.append(freq[i][inner])
                if len(ans) == k:
                    return ans
                inner += 1