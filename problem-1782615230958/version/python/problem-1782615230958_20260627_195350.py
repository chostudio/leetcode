# Last updated: 6/27/2026, 7:53:50 PM
1class Solution:
2    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
3        # merge then remove
4        occupiedIntervals.sort(key=lambda x:x[0])
5        
6        arr = []
7        for i in range(len(occupiedIntervals)):
8            if len(arr) == 0:
9                arr.append(occupiedIntervals[i])
10                continue
11            curr = occupiedIntervals[i]
12            if arr[-1][1] + 1 >= curr[0]:
13                # combine if overlap
14                arr[-1][1] = max(arr[-1][1], curr[1])
15            else: # no overlap, append:
16                arr.append(occupiedIntervals[i])
17        ans = []
18        for start, end in arr:
19            # case where we need to splti itnerval into two
20            if start < freeStart and end > freeEnd:
21                ans.append([start, min(end, freeStart-1)])
22                ans.append([max(start, freeEnd+1), end])
23            
24            elif end < freeStart or start > freeEnd:
25                ans.append([start, end])
26            # no verlap at all ^
27            # if entirely within overlap, dont add
28            elif freeStart <= start and end <= freeEnd:
29                continue
30            # if some overlap, edit the thing
31            elif end <= freeEnd:
32                ans.append([start, min(end, freeStart-1)])
33            elif start >= freeStart:
34                ans.append([max(start, freeEnd+1), end])
35            
36        return ans
37                
38        