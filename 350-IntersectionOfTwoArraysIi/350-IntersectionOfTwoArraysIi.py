# Last updated: 9/11/2025, 12:31:59 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        ans = []
        for i in nums1:
            hashmap[i] += 1
        for x in nums2:
            if hashmap[x] > 0:
                ans.append(x)
                hashmap[x] -= 1
        return ans