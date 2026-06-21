# Last updated: 6/20/2026, 7:54:59 PM
1class Solution:
2    def maxDistance(self, moves: str) -> int:
3        # you know what it could be math actually. just add too the biggest difference counting the ___
4        x, y = 0, 0
5        underscores = 0
6        for direction in moves:
7            if direction == "U":
8                y += 1
9            elif direction == "D":
10                y -= 1
11            elif direction == "R":
12                x += 1
13            elif direction == "L":
14                x -= 1
15            else:
16                underscores += 1
17        return abs(x) + abs(y) + underscores
18            
19
20
21
22
23        # backtracking try all possibilities
24        # then dp maybe
25
26        best = [0]
27        def dfs(x, y, index):
28            if index >=len(moves):
29                #reached the end calculate it
30                calc = abs(x) + abs(y)
31                best[0] = max(best[0], calc)
32                return
33            if moves[index] == "_":
34                dfs(x+1, y, index + 1)
35                dfs(x-1, y, index + 1)
36                dfs(x, y-1, index + 1)
37                dfs(x, y+1, index + 1)
38            elif moves[index] == "R":
39                dfs(x+1, y, index + 1)
40            elif moves[index] == "L":
41                dfs(x-1, y, index + 1)
42            elif moves[index] == "D":
43                dfs(x, y-1, index + 1)
44            else: # U
45                dfs(x, y+1, index + 1)
46                
47        dfs(0, 0, 0)
48        return best[0]