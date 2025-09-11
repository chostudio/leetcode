# Last updated: 9/11/2025, 12:30:37 PM
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        xy = {}

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                xy[mat[r][c]] = [r, c]

        row = defaultdict(int)
        col = defaultdict(int)

        for i in range(len(arr)):
            r, c = xy[arr[i]]
           
            row[r] += 1
            col[c] += 1
            # needed to swapp the two lens around. 
            if row[r] == len(mat[0]) or col[c] == len(mat):
                return i
        return -1