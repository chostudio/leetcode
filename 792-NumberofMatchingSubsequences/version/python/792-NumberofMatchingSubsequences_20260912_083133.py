# Last updated: 9/12/2026, 8:31:33 AM
1class Solution:
2    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
3        ans = 0
4        freq = defaultdict(int)
5        for word in words:
6            freq[word] += 1
7        # bc there's dups but you need to account for them
8
9        # if there is no char count for a letter, then no matchign subsequence, end it early
10        charcount = set()
11        for c in s:
12            charcount.add(c)
13
14        for word in freq.keys():
15            j = 0
16            # if correct, we break early, if wrong go through entire string
17            for i in range(len(s)):
18                char = s[i]
19                char2 = word[j]
20                if char2 not in charcount:
21                    break
22                if char == char2:
23                    j += 1
24                if j == len(word):
25                    ans += freq[word]
26                    break
27
28        return ans