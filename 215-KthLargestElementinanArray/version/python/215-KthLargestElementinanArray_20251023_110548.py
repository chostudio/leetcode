# Last updated: 10/23/2025, 11:05:48 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap, smallest popped out first.
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
