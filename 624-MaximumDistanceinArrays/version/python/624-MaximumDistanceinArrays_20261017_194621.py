# Last updated: 10/17/2026, 7:46:21 PM
1class Solution:
2    def maxDistance(self, arrays: list[list[int]]) -> int:
3        # we just need to find the min and max num of each array then global min and max get the two biggest and smallest ones. remember to remember which array index the numbers were from so we make sure to pick different arrays
4        # since array[i]th sorted in ascending order, just get first and last positions index
5
6        big = [-inf, -inf]
7        small = [inf, -inf]
8        big2 = [-inf, -inf]
9        small2 = [inf, -inf]
10
11        for i in range(len(arrays)):
12            biggest, smallest = arrays[i][-1], arrays[i][0]
13            if biggest >= big[0] and biggest >= big2[0]:
14                big2 = big.copy()
15                big = [biggest, i]
16            elif biggest > big2[0]:
17                big2 = [biggest, i]
18            
19            if smallest <= small[0] and smallest <= small2[0]:
20                small2 = small.copy()
21                small = [smallest, i]
22            elif smallest < small2[0]:
23                small2 = [smallest, i]
24            
25        if big[1] != small[1]: return abs(big[0]-small[0])
26        combo1 = abs(big2[0] - small[0])
27        combo2 = abs(big[0] - small2[0])
28        return max(combo1, combo2)