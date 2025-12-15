# Last updated: 12/14/2025, 5:01:01 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = defaultdict(int)
4        # letter : index
5        # this is a sliding window problem remember that, thus two pointers
6        maxlen = 0
7        l = 0
8        # imagine i as r pointer
9        for i in range(len(s)):
10            # dont want to go backwards, lagging left pointer must jump forward
11            if s[i] in seen and l <= seen[s[i]]:
12                l = seen[s[i]] + 1
13            maxlen = max(maxlen, i - l + 1)
14                
15            seen[s[i]] = i
16        return maxlen