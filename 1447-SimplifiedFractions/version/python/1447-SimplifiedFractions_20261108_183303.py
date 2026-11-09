# Last updated: 11/8/2026, 6:33:03 PM
1import math
2class Solution:
3    def simplifiedFractions(self, n: int) -> list[str]:
4        s = set()
5        # demoninator (i) would never be 1
6        for d in range(2, n + 1):
7            
8            for nu in range(1, d): # numerator would never be greater than demoninator in this question
9                gcd = math.gcd(nu, d)
10                a = nu
11                b = d
12                if gcd != 1:
13                    a = nu // gcd
14                    b = d // gcd
15                s.add((a, b))
16        
17
18        ans = []
19        for t in s:
20            a, b = t
21            val = str(a) + "/" + str(b)
22            ans.append(val)
23        return ans