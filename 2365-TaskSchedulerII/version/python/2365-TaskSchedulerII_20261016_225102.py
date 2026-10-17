# Last updated: 10/16/2026, 10:51:02 PM
1class Solution:
2    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
3
4        # in the original task scheduler quesiton, we had cpus and used a heap. 
5
6        # in this one, it seems like we only care about the task of same type, and we are blocked on how long it takes to prev same type + space. it has to be IN ORDER so we cant process next task
7
8        hashmap = defaultdict(int)
9        # task type : when task of same type can be performed
10        day = 0
11        for task in tasks:
12            day += 1
13            if task in hashmap:
14                day = max(day, hashmap[task])
15                # cannot go back days, but can go forward
16            hashmap[task] = day + space +1 # earliest day
17            # every time, it takes one day to do one task
18
19        return day