# Last updated: 8/1/2026, 10:19:12 PM
1class Solution:
2    def minAreaRect(self, points: List[List[int]]) -> int:
3        # the trick with these rectangle ones are quite fascinating. def solve this one tom morning
4        pointset = set()
5        for x, y in points:
6            pointset.add((x, y))
7        minimum = inf
8        for i in range(len(points)):
9            for j in range(i+1, len(points)):
10                x, y = points[i]
11                x2, y2 = points[j]
12
13                if x == x2 or y == y2:
14                    continue # they're on the same line, cannot determine the other two points from these two points
15                # thus they must now be different x and ys
16                x3, y3 = x, y2
17                x4, y4 = x2, y
18                if (x3, y3) not in pointset or (x4, y4) not in pointset:
19                    continue
20                else:
21                    calc = abs(x2 - x) * abs(y2 - y)
22                    minimum = min(minimum, calc)
23                
24        return minimum if minimum != inf else 0
25