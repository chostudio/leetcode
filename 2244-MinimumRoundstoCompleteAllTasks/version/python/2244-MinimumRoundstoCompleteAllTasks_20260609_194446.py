# Last updated: 6/9/2026, 7:44:46 PM
1class Solution:
2    def minimumRounds(self, tasks: List[int]) -> int:
3        
4        # count freq of each number, if there's only 1 of the number, impossible return -1 immediately.
5        # otherwise if 2, or 3 or 4 or 5 etc. it's possible to make combos of prioritizing mod 3 if it's 5 of greater then 2, edge case is if it's 4 then it's 2
6
7        freq = defaultdict(int)
8        for t in tasks:
9            freq[t] += 1
10        
11        rounds = 0
12        # ITEMMSSSS ITEMMSSS IT'S .ITEMSSSSS
13        for number, amount in freq.items():
14            if amount == 1:
15                return -1
16            rounds += amount // 3
17            if amount % 3:
18                rounds += 1 # either 1 or 2 remainder. 1 means it was 4 so we can do 2+2. if 2 that means it's like 7 so 3+3+1 == 3 + 2+2 just changing one
19        return rounds