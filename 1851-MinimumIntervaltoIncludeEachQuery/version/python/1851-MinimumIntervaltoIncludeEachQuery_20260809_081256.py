# Last updated: 8/9/2026, 8:12:56 AM
1class Solution:
2    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
3        
4        # I think its fine to simulate brute force of writing the thing for now then doing a one pass diff array would be ideal.
5
6        biggest = 0
7
8        heap = []
9        # biggest to smallest such that smaller overwrite bigger so it'll be fine
10        for l, r in intervals:
11            # by default min heap (min pop out first)
12            length = r - l + 1
13            biggest = max(biggest, r+1) # if interval ends at last we want inclusive so since arr is 0 index if 0-8 slots then we need 9 total length so + 1
14            # time based
15            heapq.heappush(heap, (l, length, r))
16        
17        mirror = [-1] * biggest
18        curr = [] # current heap of usuable ones tht started and not ended yet. this one is length, l, r, vs available one was l, length, r
19        # mark start and end on mirror arr
20        for time in range(len(mirror)):
21            # add, remove, then submit
22            while heap and heap[0][0] <= time:
23                l, length, r = heapq.heappop(heap)
24                heapq.heappush(curr, (length, l, r))
25            # we only need to remove until we find our valid smallest one, we dcare about bigger ones since we dont use them.
26            while curr and curr[0][2] < time:
27                heapq.heappop(curr)
28
29            if curr:
30                mirror[time] = curr[0][0]
31            # else: # nothing in curr heap
32            #     -1
33
34        ans = []
35        for q in queries:
36            if not q < 0 and not q > len(mirror) - 1:
37                ans.append(mirror[q])
38            else:
39                ans.append(-1)
40        return ans