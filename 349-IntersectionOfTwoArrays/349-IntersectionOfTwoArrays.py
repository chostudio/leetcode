# Last updated: 9/11/2025, 12:32:00 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # you're over thinking it. did i do this one with carson?
        # you dont care about amount of number, so it's a set instead of hash
        aset = set()
        for i in nums1:
            if i not in aset:
                aset.add(i)
        ans = []
        for i in nums2:
            if i in aset:
                ans.append(i)
                # make sure to remove so no doubles
                aset.remove(i)
        return ans
        