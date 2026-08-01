# Last updated: 8/1/2026, 7:37:17 AM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        # i think neetcode is def a little bias bc once you see the topic that give sa big hint on how to approach the question but try to this one tom morning < 5mins
4
5        stk = []
6
7        for astr in asteroids:
8            if not stk or astr > 0:
9                stk.append(astr) # positve or negative but nothing in there
10            else: # negative and something in stk, collide
11                while stk and stk[-1] > 0 and stk[-1] < abs(astr): # if negative and negative we dont mind
12                    stk.pop()
13                if stk and stk[-1] == abs(astr):
14                    stk.pop() # same val, explode
15                    continue
16                if not stk or stk[-1] < 0:
17                    # there isnt an equal and so we append left onto the thing
18                    # or negatives
19                    stk.append(astr)
20                # if stk and stk[-1] > abs(astr):
21                #     we do nothing
22        return stk
23                