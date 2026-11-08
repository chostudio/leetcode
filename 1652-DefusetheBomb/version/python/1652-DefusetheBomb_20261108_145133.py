# Last updated: 11/8/2026, 2:51:33 PM
1class Solution:
2    def decrypt(self, code: list[int], k: int) -> list[int]:
3        
4        currsum = 0
5        rever = False
6        if k < 0:
7            rever = True
8            code.reverse()
9            k = abs(k)
10        for i in range(k):
11            currsum += code[i]
12        
13        r = k
14        ans = [0] * len(code)
15        for l in range(len(code)):
16            currsum -= code[l]
17            currsum += code[r]
18            ans[l] = currsum
19            # then shift by one each
20            # l += 1 bc for loop
21            r = (r + 1) % len(code)
22        if rever == True:
23            ans.reverse()
24        return ans