# Last updated: 9/11/2025, 12:32:16 PM
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heap to init it just needf an empty arr
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            # heap!!! not nums in the len
            if len(heap) > k:
                heapq.heappop(heap)
        # return the value at the top of the MIN heap
        return heap[0]