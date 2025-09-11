# Last updated: 9/11/2025, 12:31:26 PM
import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        final = []
        while nums:
            a = heapq.heappop(nums)
            final.append(a)
        return final