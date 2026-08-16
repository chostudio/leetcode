# Last updated: 8/15/2026, 10:45:41 PM
1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        # lambda x colon x first value
4        points.sort(key=lambda x: x[0])
5
6        # line sweep if intersecgt in point
7
8        arrow = 0
9        startb, endb = points[0][0], points[0][1]
10        for index, val in enumerate(points):
11            start, end = val
12            # if completely past it
13            if start > endb:
14                # fire the arrow for the past bound
15                arrow += 1
16                startb = start
17                endb = end
18            # if overlap with the bound then we edit the bound and dont fire arrow yet
19            elif startb <= start <= endb:
20                startb = max(startb, start)
21                endb = min(endb, end)
22        arrow += 1 # one final arrow for whatevers in the curr remain
23        return arrow