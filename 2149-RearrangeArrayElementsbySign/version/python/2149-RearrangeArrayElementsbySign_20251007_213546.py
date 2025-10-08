# Last updated: 10/7/2025, 9:35:46 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        ans = [0] * len(nums)
        for i in nums:
            if i < 0:
                ans[neg] = i
                neg += 2
            else:
                ans[pos] = i
                pos += 2
            # there's no zeros so either strictly neg or pos
        return ans