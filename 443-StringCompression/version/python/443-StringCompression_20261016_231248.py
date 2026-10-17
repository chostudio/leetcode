# Last updated: 10/16/2026, 11:12:48 PM
1class Solution:
2    def compress(self, chars: list[str]) -> int:
3        
4        newlen = 0
5        # two pointer
6        l, r = 0,0
7        while r < len(chars):
8
9            while r < len(chars) and chars[r] == chars[l]:
10                r += 1
11
12            chars[newlen] = chars[l]
13            if r - l > 1:
14                count = str(r - l)
15                for i in range(len(count)):
16                    newlen += 1
17                    chars[newlen] = count[i]
18            newlen += 1
19            l = r
20            
21        return newlen
22