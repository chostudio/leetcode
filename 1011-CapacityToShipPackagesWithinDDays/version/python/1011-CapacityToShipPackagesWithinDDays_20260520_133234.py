# Last updated: 5/20/2026, 1:32:34 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        # nlog(days), O(1) space
4        lowest = inf
5        l, r = max(weights), sum(weights)
6
7
8        def traverse(boxval):
9            days =  1
10            currval = 0
11            for w in weights:
12                # new day needed
13                if currval + w > boxval:
14                    days += 1
15                    currval = 0 # YOU HAD BOX VAL HERE
16                currval += w
17            return days
18
19        while l <= r:
20            mid = (l + r) // 2
21            numofdays = traverse(mid)
22            # it worked
23            if numofdays <= days:
24                # lets risk it and go lower:
25                lowest = min(lowest, mid) #OHHHHHHHH MG we want mid bc it's the capabity amount, you had the number of days in here trying to be lowest, that's not what we want.
26                r = mid - 1
27                # since this one has the <=, the -+ 1 goes here so mid doesnt get a infinite loop
28            else: # num of days is much bigger than days, need to go bigger amount
29                # mid (where we tested rn) didnt work so mid + 1
30                l = mid + 1 # why would
31        return lowest