# Last updated: 12/14/2025, 1:38:42 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = []
4        for i in nums:
5            heapq.heappush(heap, -i)
6        
7        for i in range(k-1):
8            heapq.heappop(heap)
9        
10        return -heapq.heappop(heap)