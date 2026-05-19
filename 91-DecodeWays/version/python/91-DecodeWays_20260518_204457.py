# Last updated: 5/18/2026, 8:44:57 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        # top down
4        dp = defaultdict(int)
5
6        def recurse(i):
7            if i >= len(s):
8                return 1 # successfully made it to the end, thus return 1 way of decoding
9            
10            if s[i] == '0':
11                # actually we have to cut the recursion path here bc 0 cannot make anyt number. if theres another number b4 0 it'll be fine otherwise we have to cut the path here
12                return 0
13            
14            if i in dp: # alr visited?
15                return dp[i]
16            
17            
18            total = 0 # yes this is a numebr we're at rn but we only care about making to the end
19            
20            if s[i] == '1' and i != len(s) - 1:
21                total += recurse(i + 2)
22            elif s[i] == '2' and i != len(s) - 1 and s[i+1] in '0123456':
23                total += recurse(i + 2) # bc we can make one more double number
24            # remember we need to recurse from the single number as well too
25            total += recurse(i + 1)
26            dp[i] = total
27            return total
28        
29            
30        
31        return recurse(0)
32
33