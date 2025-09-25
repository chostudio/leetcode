# Last updated: 9/24/2025, 5:22:29 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        halfway = total // 2
        # nums1 is smaller array

        # binary search
        l, r = 0, len(nums1) - 1
        while True:
            # set up indexes
            i = (l + r) // 2 # think of it as halfway/mid point for smaller array
            j = halfway - i - 2

            # set up values
            Aleft = nums1[i] if i >= 0 else -inf
            Aright = nums1[i + 1] if i + 1 < len(nums1) else inf
            Bleft =  nums2[j] if j >= 0 else -inf
            Bright = nums2[j + 1] if j + 1 < len(nums2) else inf

            if Aleft <= Bright and Bleft <= Aright: # forgot equality operators on chance that numbers are the same
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
                else: # odd, return the minimum of the right pointers
                    return min(Aright, Bright)
            elif Aleft > Bright: # focusing on nums1 A array only
                r = i - 1
            else: # get bigger or smaller value for partition
                l = i + 1