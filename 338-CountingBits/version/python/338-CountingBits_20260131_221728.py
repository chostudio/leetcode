# Last updated: 1/31/2026, 10:17:28 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        arr = []
4        for i in range(n+1):
5            binstr = bin(i) # btw bin turn it into a string alr
6            # rookie mistake was accidentally putting "n" in bin() rather than "i" which is correct since it changes
7            count = 0
8            # first two are "0b..."
9            for j in range(2, len(binstr)):
10                if binstr[j] == "1":
11                    count += 1
12            arr.append(count)
13        return arr