# Last updated: 12/2/2025, 5:04:40 PM
1import heapq
2class Solution:
3    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
4        # go through each row and store the thing in a hedap with (amount, index) then pop from heap k times to make ans. actually u also need to do the counting part. 3 stp process. how to count faster. wait no it is heap and then bc min heap itll be smallest, 2ndsmallest so we're good
5        heap = []
6        ans = [0] * k
7        for i in range(len(mat)):
8            col = 0 # col doubles for soldier amount due to a constraint in Q that says all 1 will be leftmost b4 0s
9            while col < len(mat[0]) and mat[i][col] == 1:
10                col += 1
11                # solder amonut, row
12            heapq.heappush(heap, (col, i))
13        for i in range(k):
14            ans[i] = heapq.heappop(heap)[1]
15        return ans
16                