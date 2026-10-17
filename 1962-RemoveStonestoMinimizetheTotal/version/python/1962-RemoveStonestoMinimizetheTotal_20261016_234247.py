# Last updated: 10/16/2026, 11:42:47 PM
1import heapq # it's heapq
2
3class Solution:
4    def minStoneSum(self, piles: list[int], k: int) -> int:
5        
6        # always divide the biggest pile, put piles into a heap and max heap pop out biggest val. python max heap you need to neagte bc minheap default
7        heap = []
8        for p in piles:
9            # clarify assume p is not negative
10            heapq.heappush(heap, -p)
11        
12        for i in range(k):
13            val = heapq.heappop(heap)
14            val = abs(val)
15
16            val = math.ceil(val / 2) # we want 9 / 2 = 5 NOT 9 //2 = 4
17            if val != 0: # just in case 1 // 2 = 0
18                heapq.heappush(heap, -val)
19        
20        total = 0
21        for p in heap:
22            total += abs(p)
23        return total