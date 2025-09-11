# Last updated: 9/11/2025, 12:31:46 PM
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        hashmap = defaultdict(int)
        i = 0
        while i < len(nums2):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                hashmap[stack[-1]] = nums2[i]
                stack.pop()
            else:
                stack.append(nums2[i])
                hashmap[nums2[i]] = -1
            i += 1
        for i in nums1:
            ans.append(hashmap[i])
        return ans