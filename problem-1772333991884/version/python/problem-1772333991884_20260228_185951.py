# Last updated: 2/28/2026, 6:59:51 PM
1class Solution:
2    cost = 0
3    def minCost(self, n: int) -> int:
4
5        amount = 0
6        while n > 1:
7            n -= 1
8            amount += n
9            
10        return amount
11        # I think this is recursion. 
12
13        # def split(num):
14        #     if num == 1:
15        #         return 1
16        #     if num == 2:
17        #         self.cost += 1
18        #         return 1
19        #     a = num // 2
20        #     b = num // 2 if num % 2 == 0 else num // 2+1
21        #     self.cost += a * b
22        #     if num % 2 == 0:
23        #         split(num // 2)
24        #     else:
25        #         return split(num // 2 + 1) + split(num // 2)
26            
27        # split(n)
28        # return cost