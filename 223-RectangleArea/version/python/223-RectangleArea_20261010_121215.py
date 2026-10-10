# Last updated: 10/10/2026, 12:12:15 PM
1class Solution:
2    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
3        
4        a = abs(ay2 - ay1) * abs(ax2 - ax1)
5        b = abs(by2 - by1) * abs(bx2 - bx1)
6    
7        # This is a good problem because it deals with a lot of edge cases. The first edge case being: is there an overlap at all? 
8        
9        if ax1 <= ax2 <= bx1 <= bx2 or ax2 >= ax1 >= bx2 >= bx1:
10            return a + b
11        if ay1 <= ay2 <= by1 <= by2 or ay2 >= ay1 >= by2 >= by1:
12            return a + b
13        
14        # is the entirety of another rectangle within the other rectangle?
15        if ax1 <= bx1 <= bx2 <= ax2 and ay1 <= by1 <= by2 <= ay2:
16            return a
17        if bx1 <= ax1 <= ax2 <= bx2 and by1 <= ay1 <= ay2 <= by2:
18            return b
19        
20        # we dont know which is leftmost, rightmost, bottommost, upmost. we want to take the min/max of points
21        right, left, top, bottom = 0,0,0,0
22
23        left = max(ax1, bx1)
24        right = min(ax2, bx2)
25        bottom = max(ay1, by1)
26        up = min(ay2, by2)
27        # if ax1 <= bx1:
28        #     left = bx1
29        # else:
30        #     left = ax1 # ax1 is more right than bx1
31        
32        # if ax2 <= bx2:
33        #     right = ax2 # ax2 is mroe left than bx2
34        # else:
35        #     right = ax2
36        
37        # if by1 <= ay1:
38        #     bottom = ay1
39        # else:
40        #     bottom = by1
41        
42        # if ay2 <= by2:
43        #     up = ay2
44        # else:
45        #     up = by2
46        
47        # ohhhhhh we want the total area covered by the two rectangles. NOT the area overlap.
48        print(left, right, bottom, up)
49        # So now that we have the area of overlap
50        overlap  =  abs(right - left) * abs(up - bottom)
51
52        return a + b - overlap