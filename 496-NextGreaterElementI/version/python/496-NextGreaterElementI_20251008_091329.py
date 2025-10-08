# Last updated: 10/8/2025, 9:13:29 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = defaultdict(int)
        # (val)
        for i in range(len(nums2)):
            while len(stack)!=0 and stack[-1] < nums2[i]:
                val = stack.pop()
                hashmap[val] = nums2[i]
            stack.append((nums2[i]))
        # go through nums 2 woth stack and save what is next greater element and then loop through nums 1 and some kind of hashmap remeber O(1) time as you loop through
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                ans[i] = hashmap[nums1[i]]
                # else if we didn't check it would actually overwrite and set to 0 for some reason instead of leaving it as -1
        return ans