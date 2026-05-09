# Last updated: 5/9/2026, 3:53:09 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        n = len(heights)
4        leftmost =[-1] * n
5        rightmost = [n] * n
6        stack = []
7
8        # remembering the right and left range for how far the max val of a height can go. 
9
10        for i in range(n):
11            while stack and heights[stack[-1]] >= heights[i]:
12                # equal in the condition bc lets say it's [2,2] we would remove the prior two from the stack so that when we save the index in the left/right most array, we say that we go PAST the prior duplicate so either the index before it, or -1 if at the end of array
13                stack.pop()
14            if stack:
15                leftmost[i] = stack[-1]
16            stack.append(i)
17        
18        stack = []
19        for i in range(n-1, -1, -1):
20            while stack and heights[stack[-1]] >= heights[i]:
21                # why equal in the condition bc 
22                stack.pop()
23            if stack:
24                rightmost[i] = stack[-1]
25            stack.append(i)
26        
27        ans = 0
28        for i in range(n):
29            # remember to -1 for the width to remove the overlap. also for max edge case example is length of arr - - 1 will + 1 so we need to -1 to get length of array
30            ans = max(ans, heights[i] * (rightmost[i] - leftmost[i] -1))
31        return ans