# Last updated: 5/16/2026, 7:31:54 PM
1class Solution:
2    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
3
4        if len(s) < 2:
5            return True
6        for i in range(len(s)-1):
7            one = s[i]
8            two = s[i+1]
9            if abs(int(two)-int(one)) > 2:
10                return False
11        return True