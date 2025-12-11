# Last updated: 12/11/2025, 8:53:15 AM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        # hashmap 
4        hashmap= defaultdict(int)
5        for i in range(len(nums)):
6            if nums[i] in hashmap:
7                if abs(hashmap[nums[i]] - i ) <= k:
8                    return True
9            hashmap[nums[i]] = i
10        return False