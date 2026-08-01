# Last updated: 8/1/2026, 8:13:32 AM
1# so very first thing I thought of was this can be solvable using a heap very easily. The issue is we want this is a stack because a stack has over one push and pop when a heap has log and push and pop because it has sorted every time so stack has a advantage on this.
2# class FreqStack:
3
4#     def __init__(self):
5#         self.h = defaultdict(int)
6#         self.stk = []
7#         # If there is a tie, then most recent element should be popped so I'm thinking similar to men stack where we have the minimum at each point we would want to create a Max stack, but this one is in terms of frequency so if the value of the current max is equal to the value of the incoming number frequency then we will take the incoming number and put that one as our top one otherwise, if the current freak is biggest than we would want to append that to the stack, the issue is we would append that to the stack multiple times and so if we pop that, but we wanna go back we don't know what the second biggest is if we were to pop again that's an issue... mmmm it might work. no the isue would be say [5,7,5,7,4,5, 1] we pop 5 but 1 still in the thing?
8
9#     def push(self, val: int) -> None:
10#         self.h[val] += 1
11#         # new num is most freq
12#         if not self.stk or self.h[val] >= self.h[self.stk[-1]]:
13#             self.stk.append(val)
14#         else: # same nunmber
15#             self.stk.append(self.stk[-1])
16#         print(self.stk)
17
18#     def pop(self) -> int:
19#         # get top value, decrement, return it. how 2 set nexxt top freq vals as shift up?
20#         print(self.stk)
21#         biggest = self.stk.pop()
22#         self.h[biggest] -= 1
23#         return biggest
24
25# pop out newer
26# hashmap freq: [oldest, newer index]
27# if we go up a freq, we dont remove old freq of a number. we just leave it.
28# when we pop, we start on highest freq. then we while loop go down to the next smallest freq for the next itr as a pointer for pop / what is the max freq across all numbers
29class FreqStack:
30
31    def __init__(self):
32        # freq : [num1, num2]
33        self.h = defaultdict(list)
34        # this one keeps track of the overal freq of a number so we know which one to put it in 
35        self.numfreq = defaultdict(int)
36        # pointer to level of top freq
37        self.topfreq = 0 
38       
39
40    def push(self, val: int) -> None:
41        self.numfreq[val] += 1
42        self.topfreq = max(self.topfreq, self.numfreq[val])
43
44        pointertofreqstack = self.numfreq[val]
45        # if pointertofreqstack not in self.h:
46        #     self.h[pointertofreqstack] = []
47        self.h[pointertofreqstack].append(val)
48
49        # in this one we dont care of num is top freq or not, just append at stack level
50        # print(self.h)
51
52    def pop(self) -> int:
53        # get top value, decrement, return it. how 2 set nexxt top freq vals as shift up?
54        # poprightmove recent of it
55        biggest = self.h[self.topfreq].pop()
56        self.numfreq[biggest] -= 1
57
58        # set to next freq level if nothing in curr freq level else stay at curr freq level
59        # just had to set a base case/botom line for the lowest freq to not loop around
60        while self.h[self.topfreq] == [] and self.topfreq > 0: # not in self.h:
61            self.topfreq -= 1
62        return biggest
63
64# Your FreqStack object will be instantiated and called as such:
65# obj = FreqStack()
66# obj.push(val)
67# param_2 = obj.pop()