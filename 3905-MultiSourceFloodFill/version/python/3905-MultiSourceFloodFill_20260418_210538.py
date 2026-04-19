# Last updated: 4/18/2026, 9:05:38 PM
1class Solution:
2    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
3        # OHHHHH MY GOODNESSSSSSS the ONLY CHANGE YOU HAD TO MAKE WAS A LOGIC ERROR DURING THE CONTEST WHERE U NEEED TO APPLY THE COLOR ASAP INSTEAD OF WAITING. 
4        # bfs but need to do it in a order
5        grid = [[0] * m for i in range(n)]
6        q = deque()
7        # # sort by color first
8        sorted_data = sorted(sources, key=lambda x: x[2]) 
9
10        s = set()
11        for r, c, color in sorted_data:
12            grid[r][c] = max(color, grid[r][c])
13            s.add((r, c))        
14        for r, c in s:
15            q.append([r, c, grid[r][c]])
16        print(q)
17        while q:
18            hashmap = defaultdict(int)
19            length = len(q)
20            for i in range(length):
21                
22                r, c, color = q.popleft()
23                # grid[r][c] = color
24                
25                if r - 1 >= 0 and grid[r-1][c] == 0:
26                    hashmap[(r-1, c)] = max(color, hashmap[(r-1, c)])
27                                            
28                if r + 1 < n and grid[r+1][c] == 0:
29                    hashmap[(r+1, c)] = max(color, hashmap[(r+1, c)])
30    
31                                            
32                if c - 1 >= 0 and grid[r][c-1] == 0:
33                    hashmap[(r, c-1)] = max(color, hashmap[(r, c-1)])
34                if c + 1 < m and grid[r][c+1] == 0:
35                    hashmap[(r, c+1)] = max(color, hashmap[(r, c+1)])
36
37            for row, col in hashmap.keys():
38                q.append([row, col, hashmap[(row, col)]])
39                grid[row][col] = hashmap[(row, col)]
40            hashmap.clear()
41
42            # remove any dups by taking the biggest one
43        return grid