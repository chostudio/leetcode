# Last updated: 10/19/2026, 3:34:51 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        # s = s.split()
4        # if not space, then it's a thing
5        index, r = 0, 0
6        stk = []
7        curr = 0
8        temp = []
9        ops = ['+', '-', '*', '/']
10        for r in range(len(s)):
11            if s[r] == " ":
12                continue
13            # number, operator, number
14            
15            curr = s[r] 
16            if curr in ops: # we hit an operator, otherwise number
17                # complete the curr number
18                num = int("".join(temp))
19                temp = []
20                stk.append(num)
21                stk.append(curr)
22            else:
23                temp.append(curr) # string number to the array
24
25        
26        num = int("".join(temp))
27        stk.append(num)
28        if len(stk) == 1: return sum(stk)
29
30        # in the first pass, we put nums and operators into stack. now we have num operator num
31        # 2nd pass is mult and div do it to the thing, sub and add put in the thing, if sub then negate it. 
32        arr = [stk[0]]
33        for i in range(1, len(stk), 2):
34            op = stk[i]
35            num = stk[i+1]
36            if op == "+":
37                arr.append(num)
38            elif op == "-":
39                arr.append(-num)
40            elif op == "*":
41                arr[-1] *= num
42            elif op == "/":
43                # floor it towards zero as question wants
44                if arr[-1] < 0:
45                    arr[-1] = math.ceil(arr[-1] / num)
46                else: # positive
47                    arr[-1] //= num 
48
49        return sum(arr)