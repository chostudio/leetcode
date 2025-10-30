# Last updated: 10/29/2025, 8:26:41 PM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # O(n * 2k)
        if not nums:
            return False
        if k > len(nums):
            return False
        if k == 1:
            return True
        for i in range(len(nums) - k - k+1): # need to plus one here bruh bc if length arr 4 and k is 2 it wouldnt even run bruh
            reachend1, reachend2 = False, False
            for j in range(i, i + k-1):
                if nums[j] >= nums[j + 1]:
                    break
                if j + 1 == i + k-1:
                    reachend1 = True
            for j in range(i+k, i + k+k-1):
                if nums[j] >= nums[j + 1]: # must be strictly greater than
                    break
                if j + 1 == i + k+k-1:
                    reachend2 = True
            if reachend1 and reachend2:
                return True
        return False