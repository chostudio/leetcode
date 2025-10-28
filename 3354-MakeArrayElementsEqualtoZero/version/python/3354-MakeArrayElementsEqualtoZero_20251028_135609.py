# Last updated: 10/28/2025, 1:56:09 PM
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        numzeros = 0
        n = len(nums)
        # if max(nums) >= n: return 0 # mis read that if CURR is out of the range so the INDEX not the value
        ans = 0
        # prefix sum
        totalsum = sum(nums)
        runningsum = 0

        for i in nums:
            runningsum += i
            if i == 0:
                if runningsum == totalsum - runningsum:
                    ans += 2
                # if it differs by one then increment by 1
                elif runningsum == totalsum - runningsum -1 or runningsum == totalsum - runningsum +1:
                    ans += 1
        return ans