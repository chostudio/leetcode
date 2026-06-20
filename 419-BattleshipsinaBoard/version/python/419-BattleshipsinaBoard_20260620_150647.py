# Last updated: 6/20/2026, 3:06:47 PM
1class Solution:
2    def countBattleships(self, board: List[List[str]]) -> int:
3        count = 0
4
5        # At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
6        # ^ this makes our lives easier
7
8        def dfs(r, c):
9            # do not get OOB error
10            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "X":
11                # either L /R or U/D from this point
12                board[r][c] = "V" # visited so we dont visit again
13                dfs(r+1, c)
14                dfs(r-1, c)
15                dfs(r, c+1)
16                dfs(r, c-1)
17
18        for r in range(len(board)):
19            for c in range(len(board[0])):
20                cell = board[r][c]
21                if cell == "X":
22                    dfs(r, c) # more apt name would be mark
23                    count += 1 # we increment here instead of like inf times inside of the mark recursive function
24
25
26        return count