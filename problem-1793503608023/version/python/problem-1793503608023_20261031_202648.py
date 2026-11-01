# Last updated: 10/31/2026, 8:26:48 PM
1class Solution:
2    def countPairs(self, deliciousness: list[int]) -> int:
3        # This is two sum, but you need to count all the number of ways to make power of two first. 
4
5        twos = []
6        mod = 10 ** 9 + 7
7        for i in range(41): # 0 is important
8            twos.append(2 ** i)
9        freq = defaultdict(int)
10
11        total = 0
12        for val in deliciousness:
13            for power in twos:
14                if power - val in freq:
15                    total += freq[power - val] 
16            freq[val] += 1
17        return total % mod # you have to mod once at the end, not during the middle, it's weird
18