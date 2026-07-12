# Last updated: 7/12/2026, 11:09:15 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        # okay so this one is the have vs need for O(1) checking.
4        if len(t) > len(s): return "" # imposssible
5
6        bestlen = inf
7        start, end = 0, 0
8
9        needfreq = Counter(t) # every t char in s
10        currfreq = defaultdict(int)
11        need = len(needfreq.keys())
12        curr = 0 # curr nothing in thing at start, # of exact match we have
13        
14        # start from 0, increase till have == need, then increase left pointer as much as can to minimuze it
15
16        r, l = 0, 0
17        while r < len(s):
18            currfreq[s[r]] += 1
19            # amount matches char same both
20            # == bc its okay if we have more of one char but we dont want to increment again for same char 
21            if currfreq[s[r]] == needfreq[s[r]]:
22                curr += 1 # curr is rn have, other is need/want
23            while curr == need:
24                # update best
25                if r - l - 1 < bestlen:
26                    bestlen = min(bestlen, r - l - 1)
27                    start = l
28                    end = r
29
30                # remove char at LEFT (dont hav ea typo here for right bc u copy paste it), see what happens,
31                currfreq[s[l]] -= 1
32                # no longer equal exact?
33                if currfreq[s[l]] < needfreq[s[l]]:
34                    curr -= 1
35                
36                # increase left
37                l += 1
38            r += 1
39
40        return s[start:end+1] if bestlen != inf else ""