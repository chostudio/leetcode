# Last updated: 6/20/2026, 7:21:52 PM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        # visited
4        hashmap = defaultdict(int) # r,c = longest
5
6        def dfs(r, c):
7            if (r, c) in hashmap:
8                return hashmap[(r, c)]
9
10            currcell = matrix[r][c]
11            pathlen = 0
12            # up down left right
13            # if it's in bounds and the val is greater, then go to it. we dont need a path visited set bc the monotonic increasing guarnetees that we wont revisit a lesser value cell
14            # we dont want to add all 4 split paths togehter, rather just +1 for this cell and the greatest path out of the four then save that for this cell
15            if r - 1 >= 0 and matrix[r-1][c] > currcell:
16                pathlen = max(pathlen, dfs(r-1, c))
17            
18            if r + 1 < len(matrix) and matrix[r+1][c] > currcell:
19                pathlen = max(pathlen, dfs(r+1, c))
20            
21            if c - 1 >= 0 and matrix[r][c-1] > currcell:
22                pathlen = max(pathlen, dfs(r, c-1))
23            
24            if c + 1 < len(matrix[0]) and matrix[r][c+1] > currcell:
25                pathlen = max(pathlen, dfs(r, c+1))
26
27            
28            pathlen += 1 # do this ONCE at the end so you dont have to worry about it 4 times within the if statements
29            # technically, we'll never need to max the value here because there would never be a greater value from a point. like it would be a static path so we only need to set it once
30            hashmap[(r, c)] = pathlen
31            return pathlen
32        longest = 0
33
34        for r in range(len(matrix)):
35            for c in range(len(matrix[0])):
36                if (r, c) not in hashmap:
37                    # first cell counts as it self
38                    # you do NOT need to pass an accumulator variable as a parameter???
39                    longest = max(longest, dfs(r, c))
40
41
42
43        return longest