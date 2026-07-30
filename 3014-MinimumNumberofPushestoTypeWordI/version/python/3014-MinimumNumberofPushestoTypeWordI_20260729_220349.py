# Last updated: 7/29/2026, 10:03:49 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        freq = Counter(word)
4        # we get the freq of each letter.
5        # O(26) we want to know what is the most letter freqs, we will for every 7 letters is the 1 or 2 or 3 button presses
6        # we dont actually want to know what the letters are, just how many of each of them
7        amounts = freq.values()
8        sorted(amounts)
9        partition = 0
10        ans = 0
11        for amount in amounts:
12            # 2-9 is 8 actually, not 7
13            # first 8 is 1, 9-15 is 2 bc divison is floor
14            ans += amount * (partition // 8 + 1)
15            partition += 1
16        return ans