# Last updated: 7/12/2026, 9:10:53 PM
1class Solution:
2    def candy(self, ratings: List[int]) -> int:
3        
4        costs = [1] * len(ratings)
5
6        # left
7        prev = inf
8        for i in range(len(ratings)):
9            if ratings[i] > prev:
10                costs[i] = costs[i-1] + 1
11            prev = ratings[i]
12
13        # right
14        prev = inf
15        for i in range(len(ratings) -1, -1, -1):
16            if ratings[i] > prev:
17                # in the first pass we didnt need to worry about editing anything but in the second pass we obv want to take the bigger of the either past run or thiss run
18                costs[i] = max(costs[i], costs[i+1] + 1)
19            prev = ratings[i]
20
21        return sum(costs)
22
23        