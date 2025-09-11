# Last updated: 9/11/2025, 12:30:17 PM
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # got this on he first try in 5 mins by following the rules bruhhhh but q1 TLR
        for query in queries:
            idx = query[0]
            while idx <= query[1]:
                nums[idx] = (nums[idx] * query[3]) % (10 ** 9 + 7)
                idx += query[2]
        ans = 0
        for i in nums:
            ans ^= i
        return ans