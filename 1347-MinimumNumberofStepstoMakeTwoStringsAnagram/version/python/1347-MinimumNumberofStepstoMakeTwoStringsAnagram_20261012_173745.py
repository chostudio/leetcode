# Last updated: 10/12/2026, 5:37:45 PM
1class Solution:
2    def minSteps(self, s: str, t: str) -> int:
3        
4        letters = defaultdict(int) # how many of each letter
5
6        # gaurneteed that both strings are same length. what if they were not? how woudl algo change?
7
8        for i in range(len(s)):
9            letters[s[i]] += 1
10            letters[t[i]] -= 1
11        
12        diff = 0
13        for key, val in letters.items():
14            diff += abs(val)
15        
16        return diff//2