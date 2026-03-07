# Last updated: 3/6/2026, 6:47:18 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        # 
4        board = [["."] * n for i in range(n)]
5        ans = []
6        colSet = set()
7        posDiag = set()
8        negDiag = set()
9        
10        def backtrack(r):
11            # if we reach the end state
12            if r >= n:
13                # for some reason ythe question wants it in 1d string arr format, compress cols of a row. MIND THIS
14                copy = ["".join(row) for row in board]
15                ans.append(copy)
16                return
17            
18            for c in range(n):
19
20                if c in colSet or r + c in posDiag or r - c in negDiag:
21                    continue # alr a queen there, onto the next possible thing
22
23                # add
24                board[r][c] = "Q" # set the queen on the board
25                colSet.add(c)
26                posDiag.add(r + c)
27                negDiag.add(r - c)
28
29                # recurse
30                backtrack(r + 1)
31
32                #backtrack (remove)
33                board[r][c] = "." # remove queen from board n sets
34                colSet.remove(c)
35                posDiag.remove(r + c)
36                negDiag.remove(r - c)
37
38        backtrack(0) # we start from row 0
39        return ans