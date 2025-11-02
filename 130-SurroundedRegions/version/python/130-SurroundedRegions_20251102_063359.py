# Last updated: 11/2/2025, 6:33:59 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # flip Os touching edgeds to not O dfs then mark all non changed O to X then change T to O and all good
        # X and O not 0
        def dfs(r, c): # would only call this to flip O to T
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                # in bounds good
                if board[r][c] == "O": # then remember you haveto check if the thing is a O or not so we dont repeat/infinite go forever
                    board[r][c] = "T"
                    dfs(r+1, c)
                    dfs(r, c+1)
                    dfs(r-1, c)
                    dfs(r, c-1)
            
            return # make sure to return regardless

        # go along edges
        # side columns up and down
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][len(board[0])-1] == "O":
                dfs(r, len(board[0])-1)
        
        # top and bottom rows left to right
        for c in range(len(board[0])):
            if board[0][c] == "O":
                dfs(0, c)
            if board[len(board)-1][c] == "O":
                dfs(len(board)-1, c)
        
        # now double loop twice one to change all O to X then another to change all T back to O
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X" # accidentally had double == instead of one =
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"
