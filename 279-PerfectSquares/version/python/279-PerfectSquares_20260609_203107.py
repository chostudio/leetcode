# Last updated: 6/9/2026, 8:31:07 PM
1from collections import deque
2import math # lowercase, not uppercase like java
3class Solution:
4    def numSquares(self, n: int) -> int:
5        
6        # bfs. # generate the possible numbers then just go down the line. inefficinet tho
7
8        arr = []
9        for i in range(int(math.sqrt(n))+1):
10            arr.append(i * i)
11        arr.reverse() # biggest first
12
13        # edge case where if n is 0 then we need to return 0 otherwise bfs code has inf loop
14        if n == 0:
15            return 0
16        lowest = inf
17        q = deque()
18        q.append([n, 0])
19        # the reason we need a visited is so taht we dont calculate from the same amount. and because we're minusing, it'll always guarentee that the first occurance of a number will be the guarenteed shortest potential path than a second occurance of a number.
20        visited = set()
21        visited.add(n)
22        while q:
23            amount, freq = q.popleft()
24
25            # minus biggest first
26            for square in arr:
27                if amount - square == 0:
28                    # Since BFS explores level by level, the first solution found is guaranteed to be the shortest.
29                    return freq + 1
30                # elif amount - square < 0: # impossible, dont minus it
31                # continue
32                elif amount - square not in visited:
33                    # we add to visited set BEFORE adding such that on the next go around we prevent it from readding a duplicate e.g. if we were to mark as visited at the bfs node rather than before it that would incur duplicate adding into teh queue
34                    visited.add(amount - square)
35                    q.append([amount - square, freq + 1])
36                
37        
38        # wont return anything here bc first one found is possible.
39