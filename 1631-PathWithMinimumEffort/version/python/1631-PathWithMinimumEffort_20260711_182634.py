# Last updated: 7/11/2026, 6:26:34 PM
1class Solution:
2    def minimumEffortPath(self, heights: List[List[int]]) -> int:
3        # okay dikstra of absolute differences, always taking the smallest absolute difference based on one node to other node. 2d array of visited of a cell and the value is the smallest absolute value we've seen at that so future ones know whether to stop or keep going
4        # dikstra but we must check whether all values are positive
5        
6        heap = []
7        visited = [[inf] * len(heights[0]) for n in heights]
8        print(visited)
9        # min heap, prioritixze the smallest first
10        # we dont need abs val as a 4th thing bc biggestabsval we've seen so far does the job
11
12        m = len(heights[0])-1
13        n = len(heights)-1
14
15        # biggest absolute val so far, r, c, 
16        heapq.heappush(heap, (0, 0, 0))
17        while heap:
18            biggestsofar, r, c = heapq.heappop(heap)
19
20            if biggestsofar > visited[r][c]:
21                continue
22            if r == len(heights)-1 and c == len(heights[0])-1:
23                return biggestsofar
24            
25            # visited[r][c] = biggestsofar
26            # up down left right
27            if r > 0:
28                newabs = abs(heights[r][c]-heights[r-1][c])
29                if max(biggestsofar, newabs) < visited[r-1][c]:
30                    visited[r-1][c] = max(biggestsofar, newabs)
31                    heapq.heappush(heap, (max(biggestsofar, newabs), r-1, c))
32            if r < n:
33                newabs = abs(heights[r][c]-heights[r+1][c])
34                if max(biggestsofar, newabs) < visited[r+1][c]:
35                    visited[r+1][c] = max(biggestsofar, newabs)
36                    heapq.heappush(heap, (max(biggestsofar, newabs), r+1, c))
37            if c > 0:
38                newabs = abs(heights[r][c]-heights[r][c-1])
39                if max(biggestsofar, newabs) < visited[r][c-1]:
40                    visited[r][c-1] = max(biggestsofar, newabs)
41                    heapq.heappush(heap, (max(biggestsofar, newabs), r, c-1))
42            if c < m:
43                newabs = abs(heights[r][c]-heights[r][c+1])
44                if max(biggestsofar, newabs) < visited[r][c+1]:
45                    visited[r][c+1] = max(biggestsofar, newabs)
46                    heapq.heappush(heap, (max(biggestsofar, newabs), r, c+1))
47
48        return visited[len(heights)-1][len(heights[0])-1]