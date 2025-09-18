# Last updated: 9/17/2025, 11:06:33 PM
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        hashmap = defaultdict(int)
        ans = []
        for index, val in nums1:
            hashmap[index] += val
        for index, val in nums2:
            hashmap[index] += val
        for i in sorted(hashmap.keys()):
            ans.append([i, hashmap[i]])
        return ans