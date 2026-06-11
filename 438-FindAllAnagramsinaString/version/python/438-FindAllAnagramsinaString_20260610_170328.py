# Last updated: 6/10/2026, 5:03:28 PM
1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        if len(p) > len(s):
4            return [] # edgecase 
5        # first hash the target "p"
6        targetfreq = [0] * 26
7        for char in p:
8            targetfreq[ord(char)-ord('a')] += 1
9
10        # changing arr into tuple is O(p), len of string
11
12        ans = []
13        freq = [0] * 26
14        # then set up the initial window for s
15        for i in range(len(p)):
16            freq[ord(s[i])-ord('a')] += 1
17
18
19        plen = len(p)
20        # then slide through s
21        for i in range(len(s)-plen):
22            # in order to not have a O(26) character counting frequency check everytime, you would do a have & need two integer variables that you would increment or decrement "have" based on if a letter freq changes to matching or away from matching
23            if freq == targetfreq:
24                ans.append(i)
25            
26            # shift first and last letter
27            freq[ord(s[i])-ord('a')] -= 1
28            freq[ord(s[i+plen])-ord('a')] += 1
29
30        # you need to check at the very last index too
31        if freq == targetfreq:
32            ans.append(len(s)-len(p))
33        return ans