# Last updated: 10/23/2025, 11:16:17 AM
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap of (dist calculated, (the xy, x values)) then pop out k times or do max heap (biggest goes out first) so O(k) space max
        heap = []
        for x, y in points:
            dist = math.sqrt((x*x) + (y*y))
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap) # get rud of furthest value so keeping closest value
        ans = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans