# Last updated: 7/16/2026, 7:14:29 AM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        # actually we dont need to sort, bc heap would do that for us
4        heap = []
5        # thenput into heap, for start and removal amounts
6        for numpass, fro, to in trips:
7            heapq.heappush(heap, (fro, numpass))
8            heapq.heappush(heap, (to, -numpass))
9        
10        curramount = 0 
11        while heap:
12            index, numpass = heapq.heappop(heap)
13            curramount += numpass
14            if curramount > capacity:
15                return False
16        return True